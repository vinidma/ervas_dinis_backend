<template>
  <footer class="bg-gray-800 text-white">
    <div class="container mx-auto px-4 py-12">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Logo e Descrição -->
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-10 h-10 bg-primary-600 rounded-full flex items-center justify-center">
              <span class="text-white font-bold text-lg">ED</span>
            </div>
            <span class="text-xl font-bold">Ervas Dinis</span>
          </div>
          <p class="text-gray-300 mb-4 max-w-md">
            Especialistas em ervas medicinais e flores ornamentais. 
            Oferecemos produtos naturais de alta qualidade para seu bem-estar e decoração.
          </p>
          <div class="flex items-center space-x-2 text-primary-400">
            <TruckIcon class="w-5 h-5" />
            <span class="font-semibold">Entrega para todo o Brasil</span>
          </div>
        </div>

        <!-- Links Rápidos -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Links Rápidos</h3>
          <ul class="space-y-2">
            <li>
              <router-link to="/" class="text-gray-300 hover:text-primary-400 transition-colors">
                Início
              </router-link>
            </li>
            <li>
              <router-link to="/produtos" class="text-gray-300 hover:text-primary-400 transition-colors">
                Produtos
              </router-link>
            </li>
            <li>
              <router-link to="/sobre" class="text-gray-300 hover:text-primary-400 transition-colors">
                Sobre Nós
              </router-link>
            </li>
            <li>
              <router-link to="/contato" class="text-gray-300 hover:text-primary-400 transition-colors">
                Contato
              </router-link>
            </li>
          </ul>
        </div>

        <!-- Contato -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Contato</h3>
          <ul class="space-y-2 text-gray-300">
            <li class="flex items-center space-x-2">
              <PhoneIcon class="w-4 h-4" />
              <span>(11) 99999-9999</span>
            </li>
            <li class="flex items-center space-x-2">
              <EnvelopeIcon class="w-4 h-4" />
              <span>contato@ervasdinis.com.br</span>
            </li>
            <li class="flex items-center space-x-2">
              <MapPinIcon class="w-4 h-4" />
              <span>São Paulo, SP</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Linha divisória -->
      <div class="border-t border-gray-700 mt-8 pt-8">
        <div class="flex flex-col md:flex-row justify-between items-center">
          <p class="text-gray-400 text-sm">
            © {{ currentYear }} Ervas Dinis. Todos os direitos reservados.
          </p>
          <div class="flex space-x-4 mt-4 md:mt-0">
            <a href="#" class="text-gray-400 hover:text-primary-400 transition-colors">
              Política de Privacidade
            </a>
            <a href="#" class="text-gray-400 hover:text-primary-400 transition-colors">
              Termos de Uso
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import { computed } from 'vue'
import { TruckIcon, PhoneIcon, EnvelopeIcon, MapPinIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'Footer',
  components: {
    TruckIcon,
    PhoneIcon,
    EnvelopeIcon,
    MapPinIcon
  },
  setup() {
    const currentYear = computed(() => new Date().getFullYear())

    return {
      currentYear
    }
  }
}
</script>