import axios from 'axios'

const api = axios.create({
  baseURL: '/api/v1',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Interceptor para requisições
api.interceptors.request.use(
  (config) => {
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Interceptor para respostas
api.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error.response?.status === 404) {
      console.error('Recurso não encontrado')
    } else if (error.response?.status >= 500) {
      console.error('Erro interno do servidor')
    }
    return Promise.reject(error)
  }
)

export default api