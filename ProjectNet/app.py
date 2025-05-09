from flask import Flask, request, jsonify, send_file
import os
import uuid
from werkzeug.utils import secure_filename
from models import load_model, predict_image
from database import FileMapping, db
from utils import preprocess_image
from flask import Flask, request, jsonify
from flask_cors import CORS  # 导入 CORS

app = Flask(__name__)

# 启用 CORS，允许所有域名的请求
CORS(app)

# 配置数据库（使用SQLite）
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///results.db'  # SQLite数据库文件
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 配置文件上传文件夹
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 设置最大上传文件大小为100MB

# 确保文件夹存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# 加载模型
model = load_model()

# 预测路由
@app.route('/predict', methods=['POST'])
def predict():
    # 允许的文件类型检查
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # 保存上传文件
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(upload_path)

            # 图像预处理
            image_tensor = preprocess_image(upload_path)

            # 模型推理
            result_filename = predict_image(image_tensor, model)

            # 保存映射关系到数据库
            file_mapping = FileMapping(upload_filename=filename, result_filename=result_filename)
            db.session.add(file_mapping)
            db.session.commit()

            # 返回结果文件名给客户端
            return jsonify({'result_file': result_filename}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400


# 提供结果文件下载
@app.route('/results/<filename>', methods=['GET'])
def get_result(filename):
    result_path = os.path.join(app.config['RESULT_FOLDER'], filename)
    if os.path.exists(result_path):
        return send_file(result_path, mimetype='image/png')
    else:
        return jsonify({'error': 'Result file not found'}), 404


# 获取最近四张图片的 ID
@app.route('/recent-images', methods=['GET'])
def recent_images():
    # 获取 ID 排序最靠后的四条记录
    recent_images = FileMapping.query.order_by(FileMapping.id.desc()).limit(4).all()
    
    # 提取图片的 ID 和文件名
    image_data = [
        img.id for img in recent_images
    ]
    
    return jsonify({'recent_images': image_data})


# 获取最近十张图片的 ID
@app.route('/more-recent-images', methods=['GET'])
def more_recent_images():
    # 获取 ID 排序最靠后的四条记录
    recent_images = FileMapping.query.order_by(FileMapping.id.desc()).limit(10).all()
    
    # 提取图片的 ID 和文件名
    image_data = [
        img.id for img in recent_images
    ]
    
    return jsonify({'recent_images': image_data})


@app.route('/image/upload/<int:image_id>', methods=['GET'])
def get_upload_image(image_id):
    try:
        # 查询数据库
        file_mapping = FileMapping.query.filter_by(id=image_id).first()
        
        if file_mapping:
            # 获取上传文件路径
            upload_path = os.path.join(UPLOAD_FOLDER, file_mapping.upload_filename)
            if os.path.exists(upload_path):
                return send_file(upload_path, mimetype='image/png')
            else:
                return jsonify({'error': 'Upload image not found'}), 404
        else:
            return jsonify({'error': 'Image not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/image/result/<int:image_id>', methods=['GET'])
def get_result_image(image_id):
    try:
        # 查询数据库
        file_mapping = FileMapping.query.filter_by(id=image_id).first()
        
        if file_mapping:
            # 获取结果文件路径
            result_path = os.path.join(RESULT_FOLDER, file_mapping.result_filename)
            if os.path.exists(result_path):
                return send_file(result_path, mimetype='image/png')
            else:
                return jsonify({'error': 'Result image not found'}), 404
        else:
            return jsonify({'error': 'Image not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, threaded=False)  # 关闭多线程以确保模型安全
