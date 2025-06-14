<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Loading State -->
    <div v-if="loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
      <p class="mt-4 text-gray-600">Carregando produto...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-12">
      <p class="text-red-600 mb-4">{{ error }}</p>
      <router-link to="/produtos" class="btn-primary">
        Voltar aos Produtos
      </router-link>
    </div>

    <!-- Product Detail -->
    <div v-else-if="product" class="max-w-6xl mx-auto">
      <!-- Breadcrumb -->
      <nav class="mb-8">
        <ol class="flex items-center space-x-2 text-sm text-gray-500">
          <li><router-link to="/" class="hover:text-primary-600">Início</router-link></li>
          <li><ChevronRightIcon class="w-4 h-4" /></li>
          <li><router-link to="/produtos" class="hover:text-primary-600">Produtos</router-link></li>
          <li><ChevronRightIcon class="w-4 h-4" /></li>
          <li class="text-gray-900">{{ product.nome }}</li>
        </ol>
      </nav>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Product Image -->
        <div class="space-y-4">
          <div class="aspect-square overflow-hidden rounded-xl">
            <img 
              :src="productImage"
              :alt="product.nome"
              class="w-full h-full object-cover"
            />
          </div>
        </div>

        <!-- Product Info -->
        <div class="space-y-6">
          <div>
            <h1 class="text-3xl font-bold text-gray-900 mb-2">{{ product.nome }}</h1>
            <div class="flex items-center space-x-4">
              <span class="text-3xl font-bold text-primary-600">
                R$ {{ product.preco.toFixed(2) }}
              </span>
              <span class="text-sm text-gray-500">
                Estoque: {{ product.estoque }} unidades
              </span>
            </div>
          </div>

          <div>
            <h3 class="text-lg font-semibold mb-2">Descrição</h3>
            <p class="text-gray-700 leading-relaxed">
              {{ product.descricao || 'Produto natural de alta qualidade, cuidadosamente selecionado para oferecer os melhores benefícios.' }}
            </p>
          </div>

          <!-- Quantity Selector -->
          <div>
            <h3 class="text-lg font-semibold mb-2">Quantidade</h3>
            <div class="flex items-center space-x-4">
              <div class="flex items-center border rounded-lg">
                <button 
                  @click="decreaseQuantity"
                  :disabled="quantity <= 1"
                  class="p-2 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <MinusIcon class="w-4 h-4" />
                </button>
                <span class="px-4 py-2 min-w-[3rem] text-center">{{ quantity }}</span>
                <button 
                  @click="increaseQuantity"
                  :disabled="quantity >= product.estoque"
                  class="p-2 hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <PlusIcon class="w-4 h-4" />
                </button>
              </div>
              <span class="text-sm text-gray-500">
                Máximo: {{ product.estoque }}
              </span>
            </div>
          </div>

          <!-- Add to Cart -->
          <div class="space-y-4">
            <button 
              @click="addToCart"
              :disabled="product.estoque === 0"
              class="w-full btn-primary py-3 text-lg disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <ShoppingCartIcon class="w-5 h-5 inline mr-2" />
              {{ product.estoque === 0 ? 'Fora de Estoque' : 'Adicionar ao Carrinho' }}
            </button>
            
            <div class="grid grid-cols-2 gap-4">
              <button class="btn-outline">
                <HeartIcon class="w-4 h-4 inline mr-2" />
                Favoritar
              </button>
              <button class="btn-outline">
                <ShareIcon class="w-4 h-4 inline mr-2" />
                Compartilhar
              </button>
            </div>
          </div>

          <!-- Product Features -->
          <div class="border-t pt-6">
            <h3 class="text-lg font-semibold mb-4">Características</h3>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-center">
                <CheckIcon class="w-4 h-4 text-green-500 mr-2" />
                Produto 100% natural
              </li>
              <li class="flex items-center">
                <CheckIcon class="w-4 h-4 text-green-500 mr-2" />
                Qualidade garantida
              </li>
              <li class="flex items-center">
                <CheckIcon class="w-4 h-4 text-green-500 mr-2" />
                Entrega para todo o Brasil
              </li>
              <li class="flex items-center">
                <CheckIcon class="w-4 h-4 text-green-500 mr-2" />
                Embalagem sustentável
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useProductsStore } from '../stores/products'
import { useCartStore } from '../stores/cart'
import { 
  ChevronRightIcon,
  MinusIcon,
  PlusIcon,
  ShoppingCartIcon,
  HeartIcon,
  ShareIcon,
  CheckIcon
} from '@heroicons/vue/24/outline'

export default {
  name: 'ProductDetail',
  components: {
    ChevronRightIcon,
    MinusIcon,
    PlusIcon,
    ShoppingCartIcon,
    HeartIcon,
    ShareIcon,
    CheckIcon
  },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const route = useRoute()
    const router = useRouter()
    const productsStore = useProductsStore()
    const cartStore = useCartStore()
    
    const product = ref(null)
    const loading = ref(true)
    const error = ref(null)
    const quantity = ref(1)

    const productImage = computed(() => {
      if (!product.value) return ''
      
      const name = product.value.nome.toLowerCase()
      
      if (name.includes('flor') || name.includes('rosa') || name.includes('orquídea')) {
        return 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=800'
      } else if (name.includes('lavanda')) {
        return 'https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&w=800'
      } else {
        return 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=800'
      }
    })

    const increaseQuantity = () => {
      if (quantity.value < product.value.estoque) {
        quantity.value++
      }
    }

    const decreaseQuantity = () => {
      if (quantity.value > 1) {
        quantity.value--
      }
    }

    const addToCart = () => {
      if (product.value && product.value.estoque > 0) {
        cartStore.addToCart(product.value, quantity.value)
        cartStore.openCart()
      }
    }

    const loadProduct = async () => {
      loading.value = true
      error.value = null
      
      try {
        const productData = await productsStore.fetchProductById(props.id)
        if (productData) {
          product.value = productData
        } else {
          error.value = 'Produto não encontrado'
        }
      } catch (err) {
        error.value = 'Erro ao carregar produto'
        console.error('Erro ao carregar produto:', err)
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      loadProduct()
    })

    return {
      product,
      loading,
      error,
      quantity,
      productImage,
      increaseQuantity,
      decreaseQuantity,
      addToCart
    }
  }
}
</script>