from PIL import Image
import torchvision.transforms as transforms
import os

# 图像预处理
def preprocess_image(upload_path, testsize=352):
    transform = transforms.Compose([
        transforms.Resize((testsize, testsize)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    image = Image.open(upload_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0)
    return image_tensor


# 该方法获取文件夹中的最新四对图片文件
def get_recent_images(folder_path = "./results", num_images=4):
    # 获取文件夹中的所有文件并按修改时间排序
    files = os.listdir(folder_path)
    files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    
    # 获取文件的绝对路径并按修改时间排序
    file_paths = [os.path.join(folder_path, file) for file in files]
    file_paths.sort(key=os.path.getmtime, reverse=True)
    
    # 获取最近的四个文件
    recent_files = file_paths[:num_images]
    
    # 获取图片文件的 URL
    file_urls = [f'http://localhost:8888/{os.path.relpath(file, start="uploads")}' for file in recent_files]
    
    return file_urls

print(get_recent_images())