<template>
    <div id="app">
        <div id="header" class="container-fluid">
            <div class="row border-bottom border-dark py-3 mb-5">
                <div class="col">
                    <h1>COVID-19 Chest X-Ray Image Open Dataset Explorer</h1>
                </div>
            </div>
        </div>

        <div id="content" class="container">
            <keep-alive>
                <router-view />
            </keep-alive>
        </div>
    </div>
</template>

<style>
 #app {
     font-family: Avenir, Helvetica, Arial, sans-serif;
     -webkit-font-smoothing: antialiased;
     -moz-osx-font-smoothing: grayscale;
     text-align: center;
     color: #2c3e50;
 }

 #header {
     background-color: #dfdfdf;
 }
</style>
