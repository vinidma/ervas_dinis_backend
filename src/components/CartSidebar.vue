<template>
  <!-- Overlay -->
  <div 
    v-if="cartStore.isOpen" 
    class="fixed inset-0 bg-black bg-opacity-50 z-50"
    @click="cartStore.closeCart()"
  ></div>

  <!-- Sidebar -->
  <div 
    :class="[
      'fixed right-0 top-0 h-full w-96 bg-white shadow-xl transform transition-transform duration-300 z-50',
      cartStore.isOpen ? 'translate-x-0' : 'translate-x-full'
    ]"
  >
    <div class="flex flex-col h-full">
      <!-- Header -->
      <div class="flex items-center justify-between p-4 border-b">
        <h2 class="text-lg font-semibold">Carrinho de Compras</h2>
        <button 
          @click="cartStore.closeCart()"
          class="p-2 hover:bg-gray-100 rounded-full"
        >
          <XMarkIcon class="w-5 h-5" />
        </button>
      </div>

      <!-- Cart Items -->
      <div class="flex-1 overflow-y-auto p-4">
        <div v-if="cartStore.cartItems.length === 0" class="text-center py-8">
          <ShoppingCartIcon class="w-16 h-16 mx-auto text-gray-300 mb-4" />
          <p class="text-gray-500">Seu carrinho está vazio</p>
          <button 
            @click="cartStore.closeCart()"
            class="btn-primary mt-4"
          >
            Continuar Comprando
          </button>
        </div>

        <div v-else class="space-y-4">
          <div 
            v-for="item in cartStore.cartItems" 
            :key="item.id"
            class="flex items-center space-x-4 p-4 border rounded-lg"
          >
            <img 
              :src="getProductImage(item)"
              :alt="item.nome"
              class="w-16 h-16 object-cover rounded-lg"
            />
            <div class="flex-1">
              <h3 class="font-medium text-sm">{{ item.nome }}</h3>
              <p class="text-primary-600 font-semibold">
                R$ {{ item.preco.toFixed(2) }}
              </p>
              <div class="flex items-center space-x-2 mt-2">
                <button 
                  @click="cartStore.updateQuantity(item.id, item.quantity - 1)"
                  class="w-8 h-8 flex items-center justify-center border rounded-full hover:bg-gray-100"
                >
                  <MinusIcon class="w-4 h-4" />
                </button>
                <span class="w-8 text-center">{{ item.quantity }}</span>
                <button 
                  @click="cartStore.updateQuantity(item.id, item.quantity + 1)"
                  class="w-8 h-8 flex items-center justify-center border rounded-full hover:bg-gray-100"
                >
                  <PlusIcon class="w-4 h-4" />
                </button>
              </div>
            </div>
            <button 
              @click="cartStore.removeFromCart(item.id)"
              class="p-2 text-red-500 hover:bg-red-50 rounded-full"
            >
              <TrashIcon class="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div v-if="cartStore.cartItems.length > 0" class="border-t p-4">
        <div class="flex justify-between items-center mb-4">
          <span class="font-semibold">Total:</span>
          <span class="text-xl font-bold text-primary-600">
            R$ {{ cartStore.totalPrice.toFixed(2) }}
          </span>
        </div>
        <div class="space-y-2">
          <router-link 
            to="/carrinho"
            @click="cartStore.closeCart()"
            class="w-full btn-outline block text-center"
          >
            Ver Carrinho
          </router-link>
          <button class="w-full btn-primary">
            Finalizar Compra
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useCartStore } from '../stores/cart'
import { 
  XMarkIcon, 
  ShoppingCartIcon, 
  MinusIcon, 
  PlusIcon, 
  TrashIcon 
} from '@heroicons/vue/24/outline'

export default {
  name: 'CartSidebar',
  components: {
    XMarkIcon,
    ShoppingCartIcon,
    MinusIcon,
    PlusIcon,
    TrashIcon
  },
  setup() {
    const cartStore = useCartStore()

    const getProductImage = (product) => {
      // Retorna uma imagem placeholder baseada no tipo de produto
      const isFlower = product.nome.toLowerCase().includes('flor') || 
                      product.nome.toLowerCase().includes('rosa') ||
                      product.nome.toLowerCase().includes('orquídea')
      
      if (isFlower) {
        return 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else {
        return 'https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=400'
      }
    }

    return {
      cartStore,
      getProductImage
    }
  }
}
</script>