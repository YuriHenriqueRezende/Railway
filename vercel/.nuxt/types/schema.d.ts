import { NuxtModule, RuntimeConfig } from 'nuxt/schema'
declare module 'nuxt/schema' {
  interface NuxtConfig {
    ["primevue"]?: typeof import("nuxt-primevue").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    ["auth"]?: typeof import("@sidebase/nuxt-auth").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    ["pinia"]?: typeof import("@pinia/nuxt").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    ["devtools"]?: typeof import("@nuxt/devtools").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    ["telemetry"]?: typeof import("@nuxt/telemetry").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    modules?: (undefined | null | false | NuxtModule | string | [NuxtModule | string, Record<string, any>] | ["nuxt-primevue", Exclude<NuxtConfig["primevue"], boolean>] | ["@sidebase/nuxt-auth", Exclude<NuxtConfig["auth"], boolean>] | ["@pinia/nuxt", Exclude<NuxtConfig["pinia"], boolean>] | ["@nuxt/devtools", Exclude<NuxtConfig["devtools"], boolean>] | ["@nuxt/telemetry", Exclude<NuxtConfig["telemetry"], boolean>])[],
  }
  interface RuntimeConfig {
   app: {
      baseURL: string,

      buildAssetsDir: string,

      cdnURL: string,
   },
  }
  interface PublicRuntimeConfig {
   primevue: {
      usePrimeVue: boolean,

      resolvePath: any,

      cssLayerOrder: string,

      importPT: any,

      options: any,

      components: Array<{

      }>,

      directives: Array<{

      }>,

      composables: Array<{

      }>,

      config: Array<{

      }>,

      services: Array<{

      }>,

      styles: Array<{

      }>,

      injectStylesAsString: Array<any>,

      injectStylesAsStringToTop: Array<string>,
   },

   auth: {
      computed: {
         origin: string,

         pathname: string,

         fullBaseUrl: string,
      },

      isEnabled: boolean,

      session: {
         enableRefreshPeriodically: boolean,

         enableRefreshOnWindowFocus: boolean,
      },

      globalAppMiddleware: {
         isEnabled: boolean,

         allow404WithoutAuth: boolean,

         addDefaultCallbackUrl: boolean,
      },

      baseURL: string,

      provider: {
         type: string,

         pages: {
            login: string,
         },

         endpoints: {
            signIn: {
               path: string,

               method: string,
            },

            signOut: {
               path: string,

               method: string,
            },

            signUp: {
               path: string,

               method: string,
            },

            getSession: {
               path: string,

               method: string,
            },
         },

         token: {
            signInResponseTokenPointer: string,

            type: string,

            cookieName: string,

            headerName: string,

            maxAgeInSeconds: number,

            sameSiteAttribute: string,
         },

         sessionDataType: {
            id: string,
         },
      },
   },
  }
}
declare module 'vue' {
        interface ComponentCustomProperties {
          $config: RuntimeConfig
        }
      }