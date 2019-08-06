<template>
    <div class="single-advert">
        <div class="container">
            {{ advert.slug }}
        </div>
    </div>
</template>

<script>
import { apiService } from "@/common/api.service.js"
export default {
    name: "Advert",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
}
</script>

<style>

</style>
