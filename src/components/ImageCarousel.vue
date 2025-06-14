<template>
  <div class="relative overflow-hidden rounded-xl">
    <div class="relative h-96 md:h-[500px]">
      <transition-group name="fade" tag="div">
        <div
          v-for="(image, index) in images"
          :key="index"
          v-show="index === currentIndex"
          class="absolute inset-0"
        >
          <img
            :src="image.url"
            :alt="image.alt"
            class="w-full h-full object-cover"
          />
          <div class="absolute inset-0 bg-black bg-opacity-30"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-center text-white">
              <h2 class="text-4xl md:text-6xl font-bold mb-4">{{ image.title }}</h2>
              <p class="text-xl md:text-2xl mb-8">{{ image.subtitle }}</p>
              <router-link to="/produtos" class="btn-primary text-lg px-8 py-3">
                Ver Produtos
              </router-link>
            </div>
          </div>
        </div>
      </transition-group>
    </div>

    <!-- Navigation Arrows -->
    <button
      @click="previousSlide"
      class="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-20 hover:bg-opacity-30 text-white p-2 rounded-full transition-all duration-200"
    >
      <ChevronLeftIcon class="w-6 h-6" />
    </button>
    
    <button
      @click="nextSlide"
      class="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white bg-opacity-20 hover:bg-opacity-30 text-white p-2 rounded-full transition-all duration-200"
    >
      <ChevronRightIcon class="w-6 h-6" />
    </button>

    <!-- Dots Indicator -->
    <div class="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
      <button
        v-for="(image, index) in images"
        :key="index"
        @click="goToSlide(index)"
        :class="[
          'w-3 h-3 rounded-full transition-all duration-200',
          index === currentIndex ? 'bg-white' : 'bg-white bg-opacity-50'
        ]"
      ></button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'ImageCarousel',
  components: {
    ChevronLeftIcon,
    ChevronRightIcon
  },
  setup() {
    const currentIndex = ref(0)
    let intervalId = null

    const images = [
      {
        url: 'https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&w=1200',
        alt: 'Lavanda',
        title: 'Ervas Naturais',
        subtitle: 'Qualidade e tradição em cada produto'
      },
      {
        url: 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=1200',
        alt: 'Flores',
        title: 'Flores Ornamentais',
        subtitle: 'Beleza natural para seu lar'
      },
      {
        url: 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=1200',
        alt: 'Ervas medicinais',
        title: 'Bem-estar Natural',
        subtitle: 'Cuidando da sua saúde naturalmente'
      }
    ]

    const nextSlide = () => {
      currentIndex.value = (currentIndex.value + 1) % images.length
    }

    const previousSlide = () => {
      currentIndex.value = currentIndex.value === 0 ? images.length - 1 : currentIndex.value - 1
    }

    const goToSlide = (index) => {
      currentIndex.value = index
    }

    const startAutoplay = () => {
      intervalId = setInterval(nextSlide, 5000)
    }

    const stopAutoplay = () => {
      if (intervalId) {
        clearInterval(intervalId)
        intervalId = null
      }
    }

    onMounted(() => {
      startAutoplay()
    })

    onUnmounted(() => {
      stopAutoplay()
    })

    return {
      currentIndex,
      images,
      nextSlide,
      previousSlide,
      goToSlide
    }
  }
}
</script>