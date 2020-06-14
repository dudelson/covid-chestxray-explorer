<template>
    <div>
        <div class="row">
            <div class="col">
                <b-alert show dismissible variant="dark">
                    This webapp lets you browse xray images from the
                    <a href="https://github.com/ieee8023/covid-chestxray-dataset">
                        open dataset of COVID-19 chest x-ray images
                    </a>.
                    Click on the "view" button for any image in
                    order to view detailed data associated with that image.
                </b-alert>
            </div>
        </div>

        <div class="row row-cols-4">
            <div class="col mb-3" v-for="xray in xrays" :key="xray.id">
                <div class="card">
                    <router-link
                        :to="{name: 'view-detail', params: {id: xray.id}}"
                    >
                        <cld-image
                            class="card-img-top"
                            :publicId="'covid-chestxray-dataset/' + xray.image_url" />
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data: function () {
        return {
            xrays: []
        }
    },
    created: function () { this.fetchData(); },
    // computed: {
    //     xray_cloudinary_urls = function () {
    //         const CLOUDINARY_URL_PREFIX = ''
    //         var ret = {};
    //         for xray in this.xrays {
    //             ret[xray.id] =
    //         }
    //     };
    // },
    methods: {
        fetchData() {
            const SERVER_ENDPOINT = (process.env.NODE_ENV == 'production'
                                   ? 'https://powerful-waters-58735.herokuapp.com'
                                   : 'http://localhost:8000');
            axios.get(SERVER_ENDPOINT + '/xrays/')
                 .then(response => {
                     this.xrays = response.data;
                     const urls = this.xrays.map(xray => xray.image_url);
                     console.log(urls);
                 });
        },
    }
}
</script>
