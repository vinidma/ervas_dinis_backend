<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-8">Carrinho de Compras</h1>

    <!-- Empty Cart -->
    <div v-if="cartStore.cartItems.length === 0" class="text-center py-12">
      <ShoppingCartIcon class="w-24 h-24 mx-auto text-gray-300 mb-4" />
      <h2 class="text-2xl font-semibold mb-4">Seu carrinho está vazio</h2>
      <p class="text-gray-600 mb-8">Adicione alguns produtos para começar suas compras</p>
      <router-link to="/produtos" class="btn-primary">
        Continuar Comprando
      </router-link>
    </div>

    <!-- Cart Items -->
    <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      <!-- Items List -->
      <div class="lg:col-span-2 space-y-4">
        <div 
          v-for="item in cartStore.cartItems" 
          :key="item.id"
          class="card p-6"
        >
          <div class="flex items-center space-x-4">
            <img 
              :src="getProductImage(item)"
              :alt="item.nome"
              class="w-20 h-20 object-cover rounded-lg"
            />
            
            <div class="flex-1">
              <h3 class="font-semibold text-lg">{{ item.nome }}</h3>
              <p class="text-gray-600 text-sm">{{ item.descricao }}</p>
              <p class="text-primary-600 font-semibold text-lg">
                R$ {{ item.preco.toFixed(2) }}
              </p>
            </div>

            <div class="flex items-center space-x-4">
              <!-- Quantity Controls -->
              <div class="flex items-center border rounded-lg">
                <button 
                  @click="cartStore.updateQuantity(item.id, item.quantity - 1)"
                  class="p-2 hover:bg-gray-100"
                >
                  <MinusIcon class="w-4 h-4" />
                </button>
                <span class="px-4 py-2 min-w-[3rem] text-center">{{ item.quantity }}</span>
                <button 
                  @click="cartStore.updateQuantity(item.id, item.quantity + 1)"
                  class="p-2 hover:bg-gray-100"
                >
                  <PlusIcon class="w-4 h-4" />
                </button>
              </div>

              <!-- Remove Button -->
              <button 
                @click="cartStore.removeFromCart(item.id)"
                class="p-2 text-red-500 hover:bg-red-50 rounded-full"
              >
                <TrashIcon class="w-5 h-5" />
              </button>
            </div>
          </div>

          <!-- Item Total -->
          <div class="mt-4 pt-4 border-t flex justify-between items-center">
            <span class="text-gray-600">Subtotal:</span>
            <span class="font-semibold text-lg">
              R$ {{ (item.preco * item.quantity).toFixed(2) }}
            </span>
          </div>
        </div>
      </div>

      <!-- Order Summary -->
      <div class="lg:col-span-1">
        <div class="card p-6 sticky top-24">
          <h2 class="text-xl font-semibold mb-4">Resumo do Pedido</h2>
          
          <div class="space-y-3 mb-6">
            <div class="flex justify-between">
              <span>Subtotal ({{ cartStore.totalItems }} itens):</span>
              <span>R$ {{ cartStore.totalPrice.toFixed(2) }}</span>
            </div>
            <div class="flex justify-between">
              <span>Frete:</span>
              <span class="text-green-600">Grátis</span>
            </div>
            <div class="border-t pt-3 flex justify-between font-semibold text-lg">
              <span>Total:</span>
              <span class="text-primary-600">R$ {{ cartStore.totalPrice.toFixed(2) }}</span>
            </div>
          </div>

          <div class="space-y-3">
            <button class="w-full btn-primary py-3">
              Finalizar Compra
            </button>
            <router-link 
              to="/produtos" 
              class="w-full btn-outline block text-center py-3"
            >
              Continuar Comprando
            </router-link>
          </div>

          <!-- Security Info -->
          <div class="mt-6 pt-6 border-t">
            <div class="flex items-center space-x-2 text-sm text-gray-600">
              <ShieldCheckIcon class="w-4 h-4 text-green-500" />
              <span>Compra 100% segura</span>
            </div>
            <div class="flex items-center space-x-2 text-sm text-gray-600 mt-2">
              <TruckIcon class="w-4 h-4 text-blue-500" />
              <span>Entrega para todo o Brasil</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useCartStore } from '../stores/cart'
import { 
  ShoppingCartIcon,
  MinusIcon,
  PlusIcon,
  TrashIcon,
  ShieldCheckIcon,
  TruckIcon
} from '@heroicons/vue/24/outline'

export default {
  name: 'Cart',
  components: {
    ShoppingCartIcon,
    MinusIcon,
    PlusIcon,
    TrashIcon,
    ShieldCheckIcon,
    TruckIcon
  },
  setup() {
    const cartStore = useCartStore()

    const getProductImage = (product) => {
      const name = product.nome.toLowerCase()
      
      if (name.includes('flor') || name.includes('rosa') || name.includes('orquídea')) {
        return 'https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=400'
      } else if (name.includes('lavanda')) {
        return 'https://images.pexels.com/photos/207518/pexels-photo-207518.jpeg?auto=compress&cs=tinysrgb&w=400'
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