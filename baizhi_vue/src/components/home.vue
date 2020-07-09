<template>
    <div>
        <Header></Header>
        <Banner></Banner>
        <Footer></Footer>
    </div>
</template>

<script>

    import Header from "./commen/Header";
    import Banner from "./commen/Banner";
    import Footer from "./commen/Footer";

    export default {
        name: "Home",
        components: {
            Header: Header,
            Banner: Banner,
            Footer: Footer,
        }
    }
</script>

<style scoped>

</style>
