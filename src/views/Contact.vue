<template>
  <div class="container mx-auto px-4 py-8">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">Entre em Contato</h1>
        <p class="text-xl text-gray-600">
          Estamos aqui para ajudar! Entre em contato conosco através dos canais abaixo.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Contact Form -->
        <div class="card p-8">
          <h2 class="text-2xl font-semibold mb-6">Envie uma Mensagem</h2>
          
          <form @submit.prevent="submitForm" class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                Nome Completo *
              </label>
              <input
                type="text"
                id="name"
                v-model="form.name"
                required
                class="input-field"
                placeholder="Seu nome completo"
              />
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                E-mail *
              </label>
              <input
                type="email"
                id="email"
                v-model="form.email"
                required
                class="input-field"
                placeholder="seu@email.com"
              />
            </div>

            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">
                Telefone
              </label>
              <input
                type="tel"
                id="phone"
                v-model="form.phone"
                class="input-field"
                placeholder="(11) 99999-9999"
              />
            </div>

            <div>
              <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
                Assunto *
              </label>
              <select
                id="subject"
                v-model="form.subject"
                required
                class="input-field"
              >
                <option value="">Selecione um assunto</option>
                <option value="duvida">Dúvida sobre produtos</option>
                <option value="pedido">Informações sobre pedido</option>
                <option value="sugestao">Sugestão</option>
                <option value="reclamacao">Reclamação</option>
                <option value="outro">Outro</option>
              </select>
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
                Mensagem *
              </label>
              <textarea
                id="message"
                v-model="form.message"
                required
                rows="5"
                class="input-field resize-none"
                placeholder="Escreva sua mensagem aqui..."
              ></textarea>
            </div>

            <button
              type="submit"
              :disabled="submitting"
              class="w-full btn-primary py-3 disabled:opacity-50"
            >
              {{ submitting ? 'Enviando...' : 'Enviar Mensagem' }}
            </button>
          </form>

          <!-- Success Message -->
          <div v-if="showSuccess" class="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
            <div class="flex items-center">
              <CheckCircleIcon class="w-5 h-5 text-green-500 mr-2" />
              <span class="text-green-700">Mensagem enviada com sucesso! Entraremos em contato em breve.</span>
            </div>
          </div>
        </div>

        <!-- Contact Info -->
        <div class="space-y-8">
          <!-- Contact Details -->
          <div class="card p-8">
            <h2 class="text-2xl font-semibold mb-6">Informações de Contato</h2>
            
            <div class="space-y-4">
              <div class="flex items-start space-x-3">
                <PhoneIcon class="w-5 h-5 text-primary-600 mt-1" />
                <div>
                  <p class="font-medium">Telefone</p>
                  <p class="text-gray-600">(11) 99999-9999</p>
                  <p class="text-sm text-gray-500">Segunda a Sexta, 8h às 18h</p>
                </div>
              </div>

              <div class="flex items-start space-x-3">
                <EnvelopeIcon class="w-5 h-5 text-primary-600 mt-1" />
                <div>
                  <p class="font-medium">E-mail</p>
                  <p class="text-gray-600">contato@ervasdinis.com.br</p>
                  <p class="text-sm text-gray-500">Respondemos em até 24h</p>
                </div>
              </div>

              <div class="flex items-start space-x-3">
                <MapPinIcon class="w-5 h-5 text-primary-600 mt-1" />
                <div>
                  <p class="font-medium">Endereço</p>
                  <p class="text-gray-600">
                    Rua das Ervas, 123<br>
                    Jardim Botânico<br>
                    São Paulo - SP, 01234-567
                  </p>
                </div>
              </div>

              <div class="flex items-start space-x-3">
                <ClockIcon class="w-5 h-5 text-primary-600 mt-1" />
                <div>
                  <p class="font-medium">Horário de Funcionamento</p>
                  <p class="text-gray-600">
                    Segunda a Sexta: 8h às 18h<br>
                    Sábado: 8h às 14h<br>
                    Domingo: Fechado
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- FAQ -->
          <div class="card p-8">
            <h2 class="text-2xl font-semibold mb-6">Perguntas Frequentes</h2>
            
            <div class="space-y-4">
              <div>
                <h3 class="font-medium mb-2">Como faço um pedido?</h3>
                <p class="text-sm text-gray-600">
                  Navegue pelos nossos produtos, adicione ao carrinho e finalize a compra. 
                  É simples e seguro!
                </p>
              </div>

              <div>
                <h3 class="font-medium mb-2">Qual o prazo de entrega?</h3>
                <p class="text-sm text-gray-600">
                  Entregamos para todo o Brasil. O prazo varia de 3 a 10 dias úteis 
                  dependendo da sua localização.
                </p>
              </div>

              <div>
                <h3 class="font-medium mb-2">Os produtos são naturais?</h3>
                <p class="text-sm text-gray-600">
                  Sim! Todos os nossos produtos são 100% naturais e passam por 
                  rigoroso controle de qualidade.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { 
  PhoneIcon, 
  EnvelopeIcon, 
  MapPinIcon, 
  ClockIcon,
  CheckCircleIcon
} from '@heroicons/vue/24/outline'

export default {
  name: 'Contact',
  components: {
    PhoneIcon,
    EnvelopeIcon,
    MapPinIcon,
    ClockIcon,
    CheckCircleIcon
  },
  setup() {
    const form = ref({
      name: '',
      email: '',
      phone: '',
      subject: '',
      message: ''
    })

    const submitting = ref(false)
    const showSuccess = ref(false)

    const submitForm = async () => {
      submitting.value = true
      
      // Simula envio do formulário
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      // Reset form
      form.value = {
        name: '',
        email: '',
        phone: '',
        subject: '',
        message: ''
      }
      
      submitting.value = false
      showSuccess.value = true
      
      // Hide success message after 5 seconds
      setTimeout(() => {
        showSuccess.value = false
      }, 5000)
    }

    return {
      form,
      submitting,
      showSuccess,
      submitForm
    }
  }
}
</script>