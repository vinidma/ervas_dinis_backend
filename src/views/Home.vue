<template>
  <div>
    <!-- Hero Carousel -->
    <section class="mb-16">
      <ImageCarousel />
    </section>

    <!-- Features Section -->
    <section class="container mx-auto px-4 mb-16">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <TruckIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-2">Entrega Nacional</h3>
          <p class="text-gray-600">Enviamos para todo o Brasil com segurança e rapidez</p>
        </div>
        
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <ShieldCheckIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-2">Qualidade Garantida</h3>
          <p class="text-gray-600">Produtos naturais selecionados com o máximo cuidado</p>
        </div>
        
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <HeartIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-2">Bem-estar Natural</h3>
          <p class="text-gray-600">Cuidando da sua saúde de forma natural e sustentável</p>
        </div>
      </div>
    </section>

    <!-- Categories Section -->
    <section class="container mx-auto px-4 mb-16">
      <h2 class="text-3xl font-bold text-center mb-12">Nossas Categorias</h2>
      
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Ervas -->
        <div class="relative overflow-hidden rounded-xl group cursor-pointer" @click="$router.push('/produtos?categoria=ervas')">
          <img 
            src="https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=600"
            alt="Ervas Medicinais"
            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
          />
          <div class="absolute inset-0 bg-black bg-opacity-40 group-hover:bg-opacity-50 transition-all duration-300"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-center text-white">
              <h3 class="text-3xl font-bold mb-2">Ervas Medicinais</h3>
              <p class="text-lg">Tradição e cura natural</p>
            </div>
          </div>
        </div>

        <!-- Flores -->
        <div class="relative overflow-hidden rounded-xl group cursor-pointer" @click="$router.push('/produtos?categoria=flores')">
          <img 
            src="https://images.pexels.com/photos/56866/garden-rose-red-pink-56866.jpeg?auto=compress&cs=tinysrgb&w=600"
            alt="Flores Ornamentais"
            class="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
          />
          <div class="absolute inset-0 bg-black bg-opacity-40 group-hover:bg-opacity-50 transition-all duration-300"></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="text-center text-white">
              <h3 class="text-3xl font-bold mb-2">Flores Ornamentais</h3>
              <p class="text-lg">Beleza para seu ambiente</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Featured Products -->
    <section class="container mx-auto px-4 mb-16">
      <h2 class="text-3xl font-bold text-center mb-12">Produtos em Destaque</h2>
      
      <div v-if="productsStore.loading" class="text-center py-8">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
        <p class="mt-4 text-gray-600">Carregando produtos...</p>
      </div>

      <div v-else-if="productsStore.error" class="text-center py-8">
        <p class="text-red-600">{{ productsStore.error }}</p>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <ProductCard 
          v-for="product in featuredProducts" 
          :key="product.id" 
          :product="product" 
        />
      </div>

      <div class="text-center mt-8">
        <router-link to="/produtos" class="btn-primary">
          Ver Todos os Produtos
        </router-link>
      </div>
    </section>

    <!-- About Section -->
    <section class="bg-primary-50 py-16">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h2 class="text-3xl font-bold mb-6">Sobre a Ervas Dinis</h2>
          <p class="text-lg text-gray-700 mb-8">
            Há mais de 20 anos, a Ervas Dinis se dedica a oferecer produtos naturais de alta qualidade. 
            Nossa paixão pela natureza e pelo bem-estar das pessoas nos motiva a selecionar cuidadosamente 
            cada erva e flor que comercializamos.
          </p>
          <router-link to="/sobre" class="btn-outline">
            Conheça Nossa História
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { computed, onMounted } from 'vue'
import { useProductsStore } from '../stores/products'
import { useCartStore } from '../stores/cart'
import ImageCarousel from '../components/ImageCarousel.vue'
import ProductCard from '../components/ProductCard.vue'
import { TruckIcon, ShieldCheckIcon, HeartIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'Home',
  components: {
    ImageCarousel,
    ProductCard,
    TruckIcon,
    ShieldCheckIcon,
    HeartIcon
  },
  setup() {
    const productsStore = useProductsStore()
    const cartStore = useCartStore()

    const featuredProducts = computed(() => {
      return productsStore.products.slice(0, 4)
    })

    onMounted(async () => {
      cartStore.loadFromLocalStorage()
      await productsStore.fetchProducts()
      await productsStore.fetchCategories()
    })

    return {
      productsStore,
      featuredProducts
    }
  }
}
</script>