<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 存储图片列表
const recentImageIds = ref([])  // 初始化为空数组，避免 undefined 错误
const images = ref([])
const choosedImg = ref()

// 获取最近图片 ID 的函数
const fetchRecentImages = async () => {
    try {
        const response = await axios.get('http://localhost:8888/more-recent-images')
        recentImageIds.value = response.data.recent_images
        console.log('最近10张图片:', recentImageIds.value)
    } catch (error) {
        console.error('获取图片失败:', error)
    }
}

// 获取图片数据的函数
const fetchImages = async (imageID) => {
    try {
        const response1 = await axios.get(`http://localhost:8888/image/upload/${imageID}`, { responseType: 'blob' })
        const response2 = await axios.get(`http://localhost:8888/image/result/${imageID}`, { responseType: 'blob' })

        // 创建图片 URL 并赋值
        const image1Url = URL.createObjectURL(response1.data)
        const image2Url = URL.createObjectURL(response2.data)

        // 将图片信息推入数组
        images.value.push({
            imgId: imageID,
            uploadImageUrl: image1Url,
            resultImageUrl: image2Url
        })
    } catch (error) {
        console.error('获取图片失败:', error)
    }
}

const downloadImg = (downloadIndex) => {
    console.log(images);
    // 获取上传图片 URL 和结果图片 URL
    const resultImageUrl = images.value[downloadIndex].resultImageUrl;
    // 选择你想下载的图片，这里我默认下载 `resultImageUrl`
    const imageUrl = resultImageUrl;  // 如果没有结果图片，下载上传图片

    if (imageUrl) {
        const a = document.createElement('a');  // 创建一个临时的链接
        a.href = imageUrl;
        a.download = imageUrl.split('/').pop();  // 获取文件名作为下载名称
        document.body.appendChild(a);  // 将元素添加到 DOM 中
        a.click();  // 模拟点击
        document.body.removeChild(a);  // 下载后移除该元素
        console.log('sususususus')
    } else {
        console.error('图片 URL 不存在');
    }
};

// 在组件加载时调用
onMounted(async () => {
    await fetchRecentImages()  // 确保先获取最近图片 ID

    // 获取所有图片数据
    const imagePromises = recentImageIds.value.map(imgId => fetchImages(imgId))

    // 等待所有图片数据获取完成
    await Promise.all(imagePromises)

    // 获取完所有图片后，按 imgId 排序
    images.value.sort((a, b) => b.imgId - a.imgId )

    console.log('排序后的图片:', images.value)
})
</script>


<template>
  <main class="history-main">
    <el-table class="table_history" :data="images" stripe border>
        <el-table-column prop="imgId" label="Image_id" width="100" />

        <el-table-column label="Upload" width="200" align="center">
            <template #default="scope">
                <div class="demo-image" @click="choosedImg=scope.$index">
                    <el-image class="image-bg" :src="scope.row.uploadImageUrl" fit="fill" />
                </div>
            </template>
        </el-table-column>

        <el-table-column label="Result" width="200" align="center">
            <template #default="scope">
                <div class="demo-image" @click="choosedImg=scope.$index">
                    <el-image class="image-bg" :src="scope.row.resultImageUrl" fit="fill" />
                </div>
            </template>
        </el-table-column>

        <el-table-column label="Download Result">
            <template #default="scope">
                <el-button type="info" @click="downloadImg(scope.$index)">
                    <el-icon><Download /></el-icon>
                </el-button>
            </template>
        </el-table-column>
    </el-table>

    <div class="side-part">
        <div class="img-choose">
            <div class="img-text">Upload Img</div>
            <div class="upload">
                <el-image 
                    v-if="images[choosedImg] && images[choosedImg].uploadImageUrl" 
                    class="image-bg-choose" 
                    :src="images[choosedImg].uploadImageUrl" 
                    fit="fill" />
            </div>
        </div>

        <div class="img-choose">
            <div class="img-text">Result Img</div>
            <div class="result">  
                <el-image 
                    v-if="images[choosedImg] && images[choosedImg].resultImageUrl" 
                    class="image-bg-choose" 
                    :src="images[choosedImg].resultImageUrl" 
                    fit="fill" />
            </div>
        </div>
    </div>
  </main>
</template>

<style scoped>
.history-main {
  display: flex;
  padding: 20px;
  background-color: rgba(145, 147, 152, 0.08);
  height: 100%;
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
}

.demo-image {
    cursor: pointer;
}

.upload, .result {
    margin-left: 20%;
    margin-top: 10px;
}

.img-text {
    background-color: #dddfe5;
    padding: 4px;
    border-radius: 5px;
}

.image-bg {
    background-color: #fff;
    width: 80px;
    height: 80px;
    padding-top: 10px;
    padding-bottom: 10px;
    border-radius: 5px;
    border: #dddfe5 1px solid;
}

.image-bg-choose {
    background-color: #fff;
    width: 240px;
    height: 240px;
    padding-top: 30px;
    padding-bottom: 30px;
    border-radius: 15px;
    border: #dddfe5 1px solid;
}

.table_history {
    overflow: auto;  /* 显示滚动条，自动决定是否出现 */
    width: 60%;
    height: 100%;
}

.side-part {
    padding: 20px;
    width: 38%;
    margin-left: 20px;
    height: 100%;
    background-color: #fff;
    font-size: 20px;
}

.img-choose {
    width: 100%;
    height: 50%;
    margin-bottom: 20px;
}
</style>
