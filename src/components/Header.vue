<template>
  <header class="bg-white shadow-lg sticky top-0 z-50">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <router-link to="/" class="flex items-center space-x-2">
          <div class="w-10 h-10 bg-primary-600 rounded-full flex items-center justify-center">
            <span class="text-white font-bold text-lg">ED</span>
          </div>
          <span class="text-xl font-bold text-gray-800">Ervas Dinis</span>
        </router-link>

        <!-- Navigation -->
        <nav class="hidden md:flex items-center space-x-8">
          <router-link 
            to="/" 
            class="text-gray-700 hover:text-primary-600 font-medium transition-colors"
            active-class="text-primary-600"
          >
            Início
          </router-link>
          <router-link 
            to="/produtos" 
            class="text-gray-700 hover:text-primary-600 font-medium transition-colors"
            active-class="text-primary-600"
          >
            Produtos
          </router-link>
          <router-link 
            to="/sobre" 
            class="text-gray-700 hover:text-primary-600 font-medium transition-colors"
            active-class="text-primary-600"
          >
            Sobre
          </router-link>
          <router-link 
            to="/contato" 
            class="text-gray-700 hover:text-primary-600 font-medium transition-colors"
            active-class="text-primary-600"
          >
            Contato
          </router-link>
        </nav>

        <!-- Cart Button -->
        <div class="flex items-center space-x-4">
          <button 
            @click="cartStore.toggleCart()"
            class="relative p-2 text-gray-700 hover:text-primary-600 transition-colors"
          >
            <ShoppingCartIcon class="w-6 h-6" />
            <span 
              v-if="cartStore.totalItems > 0"
              class="absolute -top-1 -right-1 bg-primary-600 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center"
            >
              {{ cartStore.totalItems }}
            </span>
          </button>

          <!-- Mobile Menu Button -->
          <button 
            @click="mobileMenuOpen = !mobileMenuOpen"
            class="md:hidden p-2 text-gray-700"
          >
            <Bars3Icon v-if="!mobileMenuOpen" class="w-6 h-6" />
            <XMarkIcon v-else class="w-6 h-6" />
          </button>
        </div>
      </div>

      <!-- Mobile Menu -->
      <div v-if="mobileMenuOpen" class="md:hidden py-4 border-t">
        <nav class="flex flex-col space-y-4">
          <router-link 
            to="/" 
            @click="mobileMenuOpen = false"
            class="text-gray-700 hover:text-primary-600 font-medium"
          >
            Início
          </router-link>
          <router-link 
            to="/produtos" 
            @click="mobileMenuOpen = false"
            class="text-gray-700 hover:text-primary-600 font-medium"
          >
            Produtos
          </router-link>
          <router-link 
            to="/sobre" 
            @click="mobileMenuOpen = false"
            class="text-gray-700 hover:text-primary-600 font-medium"
          >
            Sobre
          </router-link>
          <router-link 
            to="/contato" 
            @click="mobileMenuOpen = false"
            class="text-gray-700 hover:text-primary-600 font-medium"
          >
            Contato
          </router-link>
        </nav>
      </div>
    </div>
  </header>
</template>

<script>
import { ref } from 'vue'
import { useCartStore } from '../stores/cart'
import { ShoppingCartIcon, Bars3Icon, XMarkIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'Header',
  components: {
    ShoppingCartIcon,
    Bars3Icon,
    XMarkIcon
  },
  setup() {
    const cartStore = useCartStore()
    const mobileMenuOpen = ref(false)

    return {
      cartStore,
      mobileMenuOpen
    }
  }
}
</script>