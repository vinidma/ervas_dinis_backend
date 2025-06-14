import { defineStore } from 'pinia'
import api from '../services/api'

export const useProductsStore = defineStore('products', {
  state: () => ({
    products: [],
    categories: [],
    loading: false,
    error: null
  }),

  getters: {
    getProductsByCategory: (state) => (categoryId) => {
      return state.products.filter(product => product.categoria_id === categoryId)
    },
    
    getProductById: (state) => (id) => {
      return state.products.find(product => product.id === parseInt(id))
    },
    
    ervas: (state) => {
      const ervasCategory = state.categories.find(cat => 
        cat.nome_categoria.toLowerCase().includes('erva')
      )
      return ervasCategory ? state.products.filter(p => p.categoria_id === ervasCategory.id) : []
    },
    
    flores: (state) => {
      const floresCategory = state.categories.find(cat => 
        cat.nome_categoria.toLowerCase().includes('flor')
      )
      return floresCategory ? state.products.filter(p => p.categoria_id === floresCategory.id) : []
    }
  },

  actions: {
    async fetchProducts() {
      this.loading = true
      this.error = null
      
      try {
        const response = await api.get('/produtos/')
        this.products = response.data
      } catch (error) {
        this.error = 'Erro ao carregar produtos'
        console.error('Erro ao buscar produtos:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchCategories() {
      this.loading = true
      this.error = null
      
      try {
        const response = await api.get('/categorias/')
        this.categories = response.data
      } catch (error) {
        this.error = 'Erro ao carregar categorias'
        console.error('Erro ao buscar categorias:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchProductById(id) {
      this.loading = true
      this.error = null
      
      try {
        const response = await api.get(`/produtos/${id}`)
        return response.data
      } catch (error) {
        this.error = 'Erro ao carregar produto'
        console.error('Erro ao buscar produto:', error)
        return null
      } finally {
        this.loading = false
      }
    }
  }
})