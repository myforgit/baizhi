<template>
    <div class="success">
        <Header/>
        <div class="main">
            <div class="title">
                <!--          <img src="../../static/images/right.svg" alt="">-->
                <div class="success-tips">
                    <p class="tips1">您已成功购买{{list_add.course_list.length}}门课程！</p>
                    <p class="tips2">你还可以加入QQ群 <span>11111111</span> 学习交流</p>
                </div>
            </div>
            <div class="order-info">
                <p class="info1"><b>付款时间：</b><span>{{list_time}}</span></p>
                <p class="info2"><b>付款金额：</b><span>￥{{list_add.real_price}}元</span></p>
                <p class="info3"><b>课程信息：</b><span
                    v-for="course in list_add.course_list">{{course.name}}/&nbsp;&nbsp; </span></p>
            </div>
            <div class="wechat-code">
            </div>
            <div class="study">
                <span><router-link to="/course">立即学习</router-link></span>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import Header from "./commen/Header";
    import Footer from "./commen/Footer";

    export default {
        name: "Payment",
        created() {
            this.payment_money();
        },
        data() {
            return {
                list_add: [],
                list_time: "",
            }
        },
        methods: {
            payment_money() {
                this.$axios.get(`${this.$settings.HOST}payment/money_apy/` + location.search,
                ).then(red => {
                    console.log(red.data);
                    this.list_add = red.data;
                    this.list_time = red.data.pay_time
                }).catch(eroor => {
                    console.log(eroor.request)
                })
            },
        },
        components: {
            Header, Footer
        },
    }
</script>

<style scoped>
    .success {
        padding-top: 80px;
    }

    .main {
        height: 100%;
        padding-top: 25px;
        padding-bottom: 25px;
        margin: 0 auto;
        width: 1200px;
        background: #fff;
    }

    .main .title {
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        padding: 25px 40px;
        border-bottom: 1px solid #f2f2f2;
    }

    .main .title .success-tips {
        box-sizing: border-box;
    }

    .title img {
        vertical-align: middle;
        width: 60px;
        height: 60px;
        margin-right: 40px;
    }

    .title .success-tips {
        box-sizing: border-box;
    }

    .title .tips1 {
        font-size: 22px;
        color: #000;
    }

    .title .tips2 {
        font-size: 16px;
        color: #4a4a4a;
        letter-spacing: 0;
        text-align: center;
        margin-top: 10px;
    }

    .title .tips2 span {
        color: #ec6730;
    }

    .order-info {
        padding: 25px 48px;
        padding-bottom: 15px;
        border-bottom: 1px solid #f2f2f2;
    }

    .order-info p {
        display: -ms-flexbox;
        display: flex;
        margin-bottom: 10px;
        font-size: 16px;
    }

    .order-info p b {
        font-weight: 400;
        color: #9d9d9d;
        white-space: nowrap;
    }

    .wechat-code {
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        padding: 25px 40px;
        border-bottom: 1px solid #f2f2f2;
    }

    .wechat-code > img {
        width: 100px;
        height: 100px;
        margin-right: 15px;
    }

    .wechat-code p {
        font-size: 14px;
        color: #d0021b;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
    }

    .wechat-code p > img {
        width: 16px;
        height: 16px;
        margin-right: 10px;
    }

    .study {
        padding: 25px 40px;
    }

    .study span {
        display: block;
        width: 140px;
        height: 42px;
        text-align: center;
        line-height: 42px;
        cursor: pointer;
        background: #ffc210;
        border-radius: 6px;
        font-size: 16px;
        color: #fff;
    }
</style>
