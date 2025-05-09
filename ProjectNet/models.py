import torch
import uuid
import os
from test import MFSNet  # 假设你的模型代码在 test.py 中
import numpy as np
import skimage.io as io
from skimage import img_as_ubyte

MODEL_PATH = './MFSNet.pth'
RESULT_FOLDER = 'results'

# 加载模型
def load_model():
    model = MFSNet()
    state_dict = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
    model.load_state_dict(state_dict)
    model.eval()
    return model

# 图像推理
def predict_image(image_tensor, model):
    with torch.no_grad():
        lateral_map_5, lateral_map_4, lateral_map_3, lateral_map_2, lateral_edge = model(image_tensor)

    # 获取结果
    res = lateral_map_2.sigmoid().data.cpu().numpy().squeeze()

    # 归一化结果
    res = (res - res.min()) / (res.max() - res.min() + 1e-8)

    # 保存结果
    result_filename = f"result_{uuid.uuid4().hex}.png"
    result_path = os.path.join(RESULT_FOLDER, result_filename)
    io.imsave(result_path, img_as_ubyte(res))

    return result_filename
