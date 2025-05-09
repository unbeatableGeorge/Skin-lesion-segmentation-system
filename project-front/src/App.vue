<script setup>
import { RouterLink, RouterView } from 'vue-router'
// import { ref } from 'vue'

</script>

<template>
  <div class="common-layout main">
    <el-container class="main">
      <el-aside class="side-bar">
        <el-col :span="24">
          <el-menu 
          default-active="1" 
          class="el-menu-vertical-demo side-menu">
            <div class="logo">
              <p> 
                <svg t="1740893712844" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2645"><path d="M603.136 939.008c-26.624 15.36-57.344 23.552-88.064 23.552s-61.44-8.192-88.064-23.552l-235.52-135.168c-54.272-31.744-88.064-91.136-88.064-153.6V374.784c0-63.488 33.792-121.856 88.064-153.6l235.52-136.192C453.632 69.632 484.352 61.44 515.072 61.44s61.44 8.192 88.064 23.552l24.576 14.336h122.88L633.856 31.744C596.992 10.24 556.032 0 515.072 0s-81.92 10.24-118.784 31.744l-235.52 136.192C86.016 210.944 40.96 289.792 40.96 374.784v273.408c0 86.016 45.056 163.84 118.784 206.848l235.52 136.192c36.864 21.504 77.824 31.744 118.784 31.744s81.92-10.24 118.784-31.744l117.76-67.584h-122.88l-24.576 15.36z" fill="#707070" p-id="2646"></path><path d="M937.984 164.864H463.872c-28.672 0-44.032 18.432-44.032 43.008v49.152h-61.44c-25.6 0-40.96 21.504-40.96 47.104v51.2c0 25.6 15.36 45.056 40.96 45.056h61.44v51.2h-61.44c-25.6 0-40.96 21.504-40.96 47.104v51.2c0 25.6 15.36 45.056 40.96 45.056h61.44v51.2h-61.44c-25.6 0-40.96 21.504-40.96 47.104v51.2c0 25.6 15.36 45.056 40.96 45.056h61.44v32.768c0 25.6 19.456 49.152 44.032 49.152h475.136c19.456 0 45.056-14.336 45.056-49.152v-614.4c-1.024-31.744-26.624-43.008-46.08-43.008zM368.64 349.184v-40.96h51.2v40.96h-51.2z m0 194.56v-40.96h51.2v40.96h-51.2z m0 194.56v-40.96h51.2v40.96h-51.2z m563.2 81.92H468.992h2.048v-604.16h460.8v604.16z" fill="#707070" p-id="2647"></path><path d="M542.72 287.744h307.2v51.2H542.72zM542.72 390.144h307.2v51.2H542.72zM727.04 523.264h-51.2v81.92h-81.92v51.2h81.92v81.92h51.2v-81.92h81.92v-51.2h-81.92z" fill="#707070" p-id="2648"></path></svg>
              </p>
              <p>
                SKIN LESION SEGMENTATION
              </p>
            </div>
            <el-menu-item index="1">  
              <RouterLink to="/" class="click-box"><el-icon><Picture /></el-icon> Upload Imgs </RouterLink>
            </el-menu-item>
            <el-menu-item index="2">
              <RouterLink to="/about" class="click-box"><el-icon><PictureRounded /></el-icon> Segmentaion Result</RouterLink>
            </el-menu-item>
            <el-menu-item index="3">
              <RouterLink to="/history" class="click-box"><el-icon><Document /></el-icon> History</RouterLink>
            </el-menu-item>
          </el-menu>
        </el-col>
        <el-icon class="icon-btm">  
          <InfoFilled />
        </el-icon>
      </el-aside>

      <el-container>
        <el-header class="app-header">
          <h3>
            Enhanced Deep Learning Models for Skin Lesion Segmentation
          </h3>
        </el-header>
        <el-main>
          <RouterView />
        </el-main>
        <el-footer class="app-footer">
          This Skin Lesion Segmentation project is developed under the supervision of Yifan Xiang, School of Computing, University of Leeds. © [2025] All rights reserved.
        </el-footer>
      </el-container>

    </el-container>
  </div>
</template>


<style scoped>
.main {
  position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}

.logo {
  margin-top: 20px;
  padding: 10px;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  svg {
    height: 50px;
    padding: 5px;
    margin-right: 10px;
    margin-left: 20px;
    border-radius: 8px;
    background-color: #eeeff2;
  }
}

.side-bar {
  position: relative;
  width: 18%;
  height: 100%;
  border-radius: 10px;
  border-right: 2px solid #eeeff2;
}

.side-menu {
  border-right: none;
}

.el-menu-item {
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  margin-bottom: 10px;
}

.el-menu-item:hover, .el-menu-item:focus {
  background-color: #eeeff2;
  .click-box {
    background-color: rgba(0,0,0,0);
  }
}

.click-box {
  color: black;
  text-decoration: none;
  transition: 0.4s;
  width: 100%;
  height: 100%;
  padding-left: 20px;
}

.icon-btm {
  position: absolute;
  bottom: 5%;
  width: 100%;
  align-items: center;
}

.app-header {
  h3 {
    font-size: 16px;
  }
  text-align: left;
  color: #666666;
  padding-top: 34px;
}

.app-footer {
  font-size: 12px;
  padding-top: 10px;
  color: #666666;
  text-align: center;
}

</style>
