<template>
  <div class="card overflow-hidden group">
    <div class="relative overflow-hidden">
      <img 
        :src="productImage"
        :alt="product.nome"
        class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
      />
      <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-300"></div>
    </div>
    
    <div class="p-4">
      <h3 class="font-semibold text-lg mb-2 text-gray-800">{{ product.nome }}</h3>
      <p class="text-gray-600 text-sm mb-3 line-clamp-2">{{ product.descricao }}</p>
      
      <div class="flex items-center justify-between mb-4">
        <span class="text-2xl font-bold text-primary-600">
          R$ {{ product.preco.toFixed(2) }}
        </span>
        <span class="text-sm text-gray-500">
          Estoque: {{ product.estoque }}
        </span>
      </div>
      
      <div class="flex space-x-2">
        <router-link 
          :to="`/produto/${product.id}`"
          class="flex-1 btn-outline text-center"
        >
          Ver Detalhes
        </router-link>
        <button 
          @click="addToCart"
          :disabled="product.estoque === 0"
          class="flex-1 btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <ShoppingCartIcon class="w-4 h-4 inline mr-1" />
          Adicionar
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { useCartStore } from '../stores/cart'
import { ShoppingCartIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'ProductCard',
  components: {
    ShoppingCartIcon
  },
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const cartStore = useCartStore()

    const productImage = computed(() => {
      // Determina a imagem baseada no nome do produto
      const name = props.product.nome.toLowerCase()
      
      if (name.includes('flor') || name.includes('rosa') || name.includes('orquídea')) {
        return 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else if (name.includes('lavanda')) {
        return 'https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else if (name.includes('alecrim')) {
        return 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else if (name.includes('manjericão')) {
        return 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else {
        return 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=400'
      }
    })

    const addToCart = () => {
      if (props.product.estoque > 0) {
        cartStore.addToCart(props.product)
      }
    }

    return {
      productImage,
      addToCart
    }
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>