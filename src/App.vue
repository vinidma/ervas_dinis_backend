<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <Header />
    <main>
      <router-view />
    </main>
    <Footer />
    <CartSidebar />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import CartSidebar from './components/CartSidebar.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    CartSidebar
  }
}
</script>