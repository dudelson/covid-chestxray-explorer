<template>
    <div class="row row-cols-2 text-left">
        <div class="col">
            <img
                class="img-fluid cld-responsive"
                :src="cloudinarySrc"
                width="auto"
                crop="scale"
            >
            <h3>Patient Facts</h3>
            <p><strong>Patient ID:</strong> {{ item.patient_id }}</p>
            <p><strong>Age:</strong> {{ item.age }}</p>
            <p><strong>Sex:</strong> {{ item.sex }}</p>
            <p><strong>Survived?</strong> {{ item.survival }}</p>
            <p><strong>Intubated?</strong> {{ item.intubated }}</p>
            <p><strong>Extubated?</strong> {{ item.extubated }}</p>
            <p><strong>Needed supplemental oxygen?</strong> {{ item.needed_supplemental_o2 }}</p>
            <p><strong>Needed ICU?</strong> {{ item.went_icu }}</p>
            <br/>
            <h3>Study Facts</h3>
            <p><strong>DOI:</strong> <a :href="item.study_url">{{ item.study_doi }}</a></p>
        </div>
        <div class="col">
            <h3>Image Facts</h3>
            <p><strong>Finding:</strong> {{ item.finding }}</p>
            <p><strong>Date Taken:</strong> {{ item.image_date }}</p>
            <p><strong>Location Taken:</strong> {{ item.location }}</p>
            <p><strong>License:</strong> {{ item.image_license }}</p>
            <p><strong>Modality:</strong> {{ item.modality }}</p>
            <p><strong>Perspective:</strong> {{ item.xray_view }}</p>
            <p><strong>Days since onset of symptoms:</strong> {{ item.offset }}</p>
            <p><strong>Taken in ICU?:</strong> {{ item.in_icu }}</p>
            <p><strong>Taken with intubation present?:</strong> {{ item.intubation_present }}</p>
            <p><strong>Patient Temperature:</strong> {{ item.temperature }}</p>
            <p><strong>Patient Oxygen Saturation:</strong> {{ item.percent_o2_saturation }}%</p>
            <p><strong>White Blood Cell Count:</strong> {{ item.wbc_count }} 10^3/uL</p>
            <p><strong>Neutrophil Cell Count:</strong> {{ item.neutrophil_count }} 10^3/uL</p>
            <p><strong>Lymphocyte Cell Count:</strong> {{ item.lymphocyte_count }} 10^3/uL</p>
            <p><strong>Clinical Notes:</strong> {{ item.clinical_notes }}</p>
            <p><strong>Other Notes:</strong> {{ item.other_notes }}</p>
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
            item: {}
        }
    },
    created: function () { this.fetchData(); },
    computed: {
        cloudinarySrc() {
            const prefix = 'covid-chestxray-dataset/';
            return cloudinaryCore.url(prefix + this.item.image_url);
        },
    },
    methods: {
        fetchData() {
            const SERVER_ENDPOINT = (process.env.NODE_ENV == 'production'
                                   ? 'https://powerful-waters-58735.herokuapp.com'
                                   : 'http://localhost:8000');
            axios.get(SERVER_ENDPOINT + '/xrays/' + this.$route.params.id + '/')
                 .then(response => {
                     this.item = response.data;
                 });
        },
    },
}
</script>
