<template>
    <div class="row row-cols-2 text-left">
        <div class="col">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg" alt="">
            <p><strong>Item ID:</strong> {{ this.$route.params.id }} </p>
            <br/>
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
export default {
    data: function () {
        return {
            item: {
                "age": 45,
                "clinical_notes": "clear regression of the areas of hypodiaphania previously appreciable bilaterally, in particular in both the upper lung fields and the right lung base.",
                "extubated": null,
                "finding": "COVID-19",
                "id": 234,
                "image_date": null,
                "image_license": "",
                "image_url": "covid-19-caso-70-2-APS.jpg",
                "in_icu": null,
                "intubated": null,
                "intubation_present": null,
                "location": "Italy",
                "lymphocyte_count": null,
                "modality": "X-ray",
                "needed_supplemental_o2": null,
                "neutrophil_count": null,
                "offset": 4,
                "other_notes": "Credit to Sergio MargariASST Fatebenefratelli Sacco � Milan",
                "patient_id": "139",
                "percent_o2_saturation": null,
                "sex": "M",
                "study_doi": "",
                "study_url": "https://www.sirm.org/2020/03/30/covid-19-caso-70/",
                "survival": null,
                "temperature": null,
                "wbc_count": null,
                "went_icu": null,
                "xray_view": "AP Supine"
            }
        }
    }
}
</script>
