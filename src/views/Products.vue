<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Header -->
    <div class="mb-8">
      <h1 class="text-3xl font-bold mb-4">Nossos Produtos</h1>
      <p class="text-gray-600">Descubra nossa seleção de ervas medicinais e flores ornamentais</p>
    </div>

    <!-- Filters -->
    <div class="mb-8">
      <div class="flex flex-wrap gap-4 items-center">
        <button 
          @click="selectedCategory = null"
          :class="[
            'px-4 py-2 rounded-lg font-medium transition-colors',
            selectedCategory === null ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          ]"
        >
          Todos
        </button>
        <button 
          @click="selectedCategory = 'ervas'"
          :class="[
            'px-4 py-2 rounded-lg font-medium transition-colors',
            selectedCategory === 'ervas' ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          ]"
        >
          Ervas
        </button>
        <button 
          @click="selectedCategory = 'flores'"
          :class="[
            'px-4 py-2 rounded-lg font-medium transition-colors',
            selectedCategory === 'flores' ? 'bg-primary-600 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          ]"
        >
          Flores
        </button>
      </div>
    </div>

    <!-- Loading State -->
    <div v-if="productsStore.loading" class="text-center py-12">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto"></div>
      <p class="mt-4 text-gray-600">Carregando produtos...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="productsStore.error" class="text-center py-12">
      <p class="text-red-600 mb-4">{{ productsStore.error }}</p>
      <button @click="loadProducts" class="btn-primary">
        Tentar Novamente
      </button>
    </div>

    <!-- Products Grid -->
    <div v-else-if="filteredProducts.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
      <ProductCard 
        v-for="product in filteredProducts" 
        :key="product.id" 
        :product="product" 
      />
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-12">
      <div class="w-24 h-24 bg-gray-200 rounded-full flex items-center justify-center mx-auto mb-4">
        <MagnifyingGlassIcon class="w-12 h-12 text-gray-400" />
      </div>
      <h3 class="text-xl font-semibold mb-2">Nenhum produto encontrado</h3>
      <p class="text-gray-600 mb-4">Não encontramos produtos para os filtros selecionados.</p>
      <button @click="selectedCategory = null" class="btn-primary">
        Ver Todos os Produtos
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useProductsStore } from '../stores/products'
import ProductCard from '../components/ProductCard.vue'
import { MagnifyingGlassIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'Products',
  components: {
    ProductCard,
    MagnifyingGlassIcon
  },
  setup() {
    const route = useRoute()
    const productsStore = useProductsStore()
    const selectedCategory = ref(null)

    const filteredProducts = computed(() => {
      if (!selectedCategory.value) {
        return productsStore.products
      }

      if (selectedCategory.value === 'ervas') {
        return productsStore.ervas
      }

      if (selectedCategory.value === 'flores') {
        return productsStore.flores
      }

      return productsStore.products
    })

    const loadProducts = async () => {
      await productsStore.fetchProducts()
      await productsStore.fetchCategories()
    }

    // Watch for route query changes
    watch(() => route.query.categoria, (newCategory) => {
      if (newCategory) {
        selectedCategory.value = newCategory
      }
    }, { immediate: true })

    onMounted(() => {
      loadProducts()
    })

    return {
      productsStore,
      selectedCategory,
      filteredProducts,
      loadProducts
    }
  }
}
</script>