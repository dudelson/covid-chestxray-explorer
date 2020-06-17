<template>
    <div>
        <div class="row">
            <div class="col">
                <b-alert variant="dark" dismissible v-model="showInfoBox">
                    This webapp lets you browse xray images from the
                    <a href="https://github.com/ieee8023/covid-chestxray-dataset">
                        open dataset of COVID-19 chest x-ray images
                    </a>.
                    Click on an image to view detailed data about it.
                </b-alert>
            </div>
        </div>

        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4">
            <div class="col mb-3" v-for="xray in paginatedXrays" :key="xray.id">
                <div class="card">
                    <router-link
                        :to="{name: 'view-detail', params: {id: xray.id}}"
                    >
                        <img
                            class="card-img-top cld-responsive"
                            :src="cloudinarySrc(xray)"
                            width="auto"
                            crop="scale"
                        >
                    </router-link>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <b-pagination-nav
                    :number-of-pages="totalPages"
                    base-url="/gallery/"
                    align="center"
                    use-router
                />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import cloudinary from 'cloudinary-core';

const cloudinaryCore = new cloudinary.Cloudinary({ cloud_name: 'dmcs4ohin' });

export default {
    data: function () {
        return {
            xrays: [],
            cardsPerPage: 100,
            showInfoBox: true,
        }
    },
    created: function () { this.fetchData(); },
    computed: {
        paginatedXrays() {
            var cur_page = this.$route.params.pagenum;
            var start = this.cardsPerPage * (cur_page-1);
            return this.xrays.slice(start, start + this.cardsPerPage);
        },
        totalPages() {
            return Math.ceil(this.xrays.length / this.cardsPerPage);
        }
    },
    methods: {
        fetchData() {
            const SERVER_ENDPOINT = (process.env.NODE_ENV == 'production'
                                   ? 'https://powerful-waters-58735.herokuapp.com'
                                   : 'http://localhost:8000');
            axios.get(SERVER_ENDPOINT + '/xrays/')
                 .then(response => {
                     this.xrays = response.data;
                 });
        },
        cloudinarySrc(xray) {
            const prefix = 'covid-chestxray-dataset/';
            return cloudinaryCore.url(prefix + xray.image_url);
        },
    }
}
</script>
