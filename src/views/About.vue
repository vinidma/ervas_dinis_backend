<template>
  <div class="container mx-auto px-4 py-8">
    <!-- Hero Section -->
    <section class="text-center mb-16">
      <h1 class="text-4xl font-bold mb-6">Sobre a Ervas Dinis</h1>
      <p class="text-xl text-gray-600 max-w-3xl mx-auto">
        Há mais de duas décadas dedicados ao cultivo e comercialização de ervas medicinais 
        e flores ornamentais, sempre priorizando a qualidade e o bem-estar dos nossos clientes.
      </p>
    </section>

    <!-- Story Section -->
    <section class="mb-16">
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
        <div>
          <img 
            src="https://images.pexels.com/photos/4750274/pexels-photo-4750274.jpeg?auto=compress&cs=tinysrgb&w=800"
            alt="Nossa história"
            class="w-full h-96 object-cover rounded-xl"
          />
        </div>
        <div>
          <h2 class="text-3xl font-bold mb-6">Nossa História</h2>
          <div class="space-y-4 text-gray-700">
            <p>
              A Ervas Dinis nasceu da paixão pela natureza e pelo conhecimento tradicional 
              sobre plantas medicinais. Fundada em 2000, nossa empresa começou como um pequeno 
              cultivo familiar e cresceu para se tornar uma referência no setor.
            </p>
            <p>
              Ao longo dos anos, desenvolvemos parcerias com produtores locais e investimos 
              em tecnologia para garantir que nossos produtos mantenham suas propriedades 
              naturais e cheguem frescos até você.
            </p>
            <p>
              Hoje, atendemos clientes em todo o Brasil, sempre mantendo nosso compromisso 
              com a qualidade, sustentabilidade e o respeito pela natureza.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Values Section -->
    <section class="mb-16">
      <h2 class="text-3xl font-bold text-center mb-12">Nossos Valores</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <HeartIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-3">Qualidade</h3>
          <p class="text-gray-600">
            Selecionamos cuidadosamente cada produto, garantindo a máxima qualidade 
            e eficácia de nossas ervas e flores.
          </p>
        </div>
        
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <GlobeAltIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-3">Sustentabilidade</h3>
          <p class="text-gray-600">
            Praticamos agricultura sustentável e utilizamos embalagens ecológicas, 
            respeitando o meio ambiente.
          </p>
        </div>
        
        <div class="text-center">
          <div class="w-16 h-16 bg-primary-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <UsersIcon class="w-8 h-8 text-primary-600" />
          </div>
          <h3 class="text-xl font-semibold mb-3">Confiança</h3>
          <p class="text-gray-600">
            Construímos relacionamentos duradouros com nossos clientes baseados 
            na transparência e confiança mútua.
          </p>
        </div>
      </div>
    </section>

    <!-- Team Section -->
    <section class="mb-16">
      <h2 class="text-3xl font-bold text-center mb-12">Nossa Equipe</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="text-center">
          <div class="w-32 h-32 bg-gray-300 rounded-full mx-auto mb-4"></div>
          <h3 class="text-xl font-semibold mb-2">Dinis Silva</h3>
          <p class="text-primary-600 mb-2">Fundador & CEO</p>
          <p class="text-gray-600 text-sm">
            Especialista em plantas medicinais com mais de 25 anos de experiência.
          </p>
        </div>
        
        <div class="text-center">
          <div class="w-32 h-32 bg-gray-300 rounded-full mx-auto mb-4"></div>
          <h3 class="text-xl font-semibold mb-2">Maria Santos</h3>
          <p class="text-primary-600 mb-2">Diretora de Qualidade</p>
          <p class="text-gray-600 text-sm">
            Farmacêutica responsável pelo controle de qualidade de todos os produtos.
          </p>
        </div>
        
        <div class="text-center">
          <div class="w-32 h-32 bg-gray-300 rounded-full mx-auto mb-4"></div>
          <h3 class="text-xl font-semibold mb-2">João Oliveira</h3>
          <p class="text-primary-600 mb-2">Gerente de Produção</p>
          <p class="text-gray-600 text-sm">
            Engenheiro agrônomo especializado em cultivo sustentável.
          </p>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="bg-primary-50 rounded-xl p-8 text-center">
      <h2 class="text-3xl font-bold mb-4">Faça Parte da Nossa História</h2>
      <p class="text-gray-700 mb-6 max-w-2xl mx-auto">
        Descubra nossos produtos naturais e experimente a diferença que a qualidade 
        e o cuidado fazem. Junte-se aos milhares de clientes satisfeitos.
      </p>
      <div class="space-x-4">
        <router-link to="/produtos" class="btn-primary">
          Ver Produtos
        </router-link>
        <router-link to="/contato" class="btn-outline">
          Entre em Contato
        </router-link>
      </div>
    </section>
  </div>
</template>

<script>
import { HeartIcon, GlobeAltIcon, UsersIcon } from '@heroicons/vue/24/outline'

export default {
  name: 'About',
  components: {
    HeartIcon,
    GlobeAltIcon,
    UsersIcon
  }
}
</script>