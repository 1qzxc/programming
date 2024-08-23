<template>
  <Layout >

    <v-container>
 
          <v-tabs v-model="tab" grow>
            <v-tab>All Events</v-tab>
            <v-tab>Live Music</v-tab>
            <v-tab>Coding Events</v-tab>
          </v-tabs>
          <v-row class="justify-space-around">

          <v-card
            v-for="edge in events" :key="edge.node.id"
            width="280"
            class="mt-5"
          >
            
          <v-img
          class="white--text align-end"
          height="200px"
          :src="`http://morozovme.com:1337${edge.node.thumbnail}`"
          />

            <v-card-title>
              {{ edge.node.title }}
            </v-card-title>
        
            <v-card-subtitle class="pb-0">
              {{ edge.node.date }}
            </v-card-subtitle>
        
            <v-card-actions>
              <v-btn
                @click="$router.push(`/events/${edge.node.id}`)"
                color="orange lighten-2"
                text
              >
                Explore
              </v-btn>
        
              <v-spacer></v-spacer>
        

            </v-card-actions>
        

          </v-card>

      </v-row>
    </v-container>
  </Layout>
</template>

<page-query>
query{
    events: allEvent{
      edges{
        node{ 
          id
          title
          description
          price
          duration
          date
          thumbnail
          image
          category
        }
      }
    }
  }
</page-query>

<script>
import moment from 'moment'

export default {
  metaInfo: {
    title: 'Hello, world!'
  },
  data() {
    return {
      tab: 0,
      events: []
    }
  },
    mounted() {
    this.events = this.$page.events.edges
  },
  watch: {
    tab(val){
      console.log(val)
      if (this.tab === 0) {
        this.showAllEvents()
      } else {
        this.showEventsByType(val)
      }
    }
  },
  methods: {
    showAllEvents() {
      this.events = this.$page.events.edges
    },
    showEventsByType(val) {
      this.categoryMap = ["0", "6196ff6335fe89002e389f87", "6196ff5535fe89002e389f86"]
      this.events = this.$page.events.edges.filter((edge) => {
        return edge.node.category === this.categoryMap[val]
      })
    }
  },
      formatDate(date) {
      return moment(date).format('MMMM Do YYYY, h:mm a')
    },
    getEvents(searchText) {
      return this.events.filter((edge) => {
        return edge.node.title.toLowerCase().includes(searchText.toLowerCase())
      })
    }
}
</script>

<style>
.home-links a {
  margin-right: 1rem;
}
</style>
