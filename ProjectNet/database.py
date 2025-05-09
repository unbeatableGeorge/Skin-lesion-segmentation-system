from flask_sqlalchemy import SQLAlchemy

# 初始化数据库
db = SQLAlchemy()

# 创建数据库模型
class FileMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload_filename = db.Column(db.String(100), nullable=False)
    result_filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<FileMapping {self.upload_filename} -> {self.result_filename}>"
