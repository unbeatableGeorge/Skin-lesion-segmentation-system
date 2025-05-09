<script setup>
import { ref } from 'vue'
import Image from "../components/Image.vue"
import { onMounted } from 'vue'
import axios from "axios"

// 获取最近四张图片
const recentImageIds = ref()
const fetchRecentImages = async () => {
    try {
        const response = await axios.get('http://localhost:8888/recent-images')
        recentImageIds.value = response.data.recent_images
        console.log('最近四张图片:', recentImageIds.value)
    } catch (error) {
        console.error('获取图片失败:', error)
    }
}

// 在组件加载时调用
onMounted(() => {
    fetchRecentImages()
})

</script>

<template>
  <div class="home-main">
    <div v-for="imageId in recentImageIds" :key="imageId">
      <Image :imgId="imageId"/>
    </div>
  </div>
</template>

<style scoped>
.home-main {
  display: flex;
  padding: 20px;
  background-color: rgba(145, 147, 152, 0.08);
  height: 100%;
  width: 100%;
  border-radius: 8px;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

</style>
