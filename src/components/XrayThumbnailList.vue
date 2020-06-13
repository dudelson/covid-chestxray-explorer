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
                    <img class="card-img-top" :src="xray.image_url" alt="Patient: Seymour Bones">
                    <div class="card-body">
                        <h5 class="card-title">My Cool Xray Image</h5>
                        <p class="card-text">My Cool Xray Image Description</p>
                        <router-link
                            class="btn btn-primary"
                            :to="{name: 'view-detail', params: {id: xray.id}}"
                        >
                            View
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data: function () {
        return {
            xrays: [
                {
                    id: 1,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
                {
                    id: 2,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
                {
                    id: 3,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
                {
                    id: 4,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
                {
                    id: 5,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
                {
                    id: 6,
                    image_url: 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Lung_X-ray.jpg/330px-Lung_X-ray.jpg'
                },
            ]
        }
    }
}
</script>
