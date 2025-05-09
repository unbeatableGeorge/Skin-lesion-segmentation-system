<script setup>
import { ref, watchEffect} from 'vue'
import axios from 'axios'

const { imgId } = defineProps(['imgId'])

// 存储图片的 URL
const imageUrl1 = ref('')
const imageUrl2 = ref('')

const fetchImages = async (imageID) => {
    try {
        const response1 = await axios.get(`http://localhost:8888/image/upload/${imageID}`, { responseType: 'blob' })
        const response2 = await axios.get(`http://localhost:8888/image/result/${imageID}`, { responseType: 'blob' })
        // 创建图片 URL 并赋值
        imageUrl1.value = URL.createObjectURL(response1.data)
        imageUrl2.value = URL.createObjectURL(response2.data)
    } catch (error) {
        console.error('获取图片失败:', error)
    }
}


watchEffect(() => {
  // 只运行一次
  fetchImages(imgId)
})

</script>

<template>
    <el-card class="box-card">
        <template #header>
            <div class="card-header">
                <span>Segmentation ID: {{ imgId }}</span>
                <el-button class="button" text><el-icon><Delete /></el-icon></el-button>
            </div>
        </template>

        <div class="card-content">
            <div class="demo-image">
                <el-image class="image-bg" :src="imageUrl1" fit="contain" />
            </div>
            <el-icon size="20px"><Right /></el-icon>
            <div class="demo-image">
                <el-image class="image-bg" :src="imageUrl2" fit="fill" />
            </div>
        </div>

        <!-- <template #footer>
            Footer content
        </template> -->
    </el-card>

</template>

<style scoped>
.image-bg {
    background-color: #fff;
    width: 160px;
    height: 160px;
    padding-top: 20px;
    padding-bottom: 20px;
    border-radius: 5px;
    border: #dddfe5 1px solid;
}

.card-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}


.box-card {
    width: 440px;
}
</style>