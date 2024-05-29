<script setup lang="ts">
import { ref } from "vue";

const itensMenu = ref([
  {
    label: "Home",
    icon: "pi pi-home",
  },
  {
    label: "Carrinho",
    icon: "pi pi-wallet",
  },
  {
    label: "Login",
    icon: "pi pi-user",
  },
]);
</script>

<template>
  <header>
    <div class="flex align-items-center justify-content-center">
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/">Catalogo</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-wallet mr-1"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-user mr-1"></i>
          <NuxtLink to="/login">Login</NuxtLink>
        </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  width: 100vw;
  height: var(--altura-header);
  border-bottom: 1px solid black;

  .menu-item{
    height: var(--altura-header);
    
    a{
      text-decoration: none;
      color: black;
    }
    &:hover{
      transform: scale(1.1);
    }
  }
}
</style>
