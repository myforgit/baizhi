<template>
    <div class="footer">
        <ul>
            <li v-for="(vre , index) in foot_list" :key="index">
              <span>{{vre.title}}</span>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Footer",
        data(){
        return{
          foot_list:[]
        }
        },
        created(){
          this.fot_lis()
        },
          methods:{
            fot_lis(){
              this.$axios({
                url:this.$settings.HOST+"home/fle/",
                methods: "get",
              }).then(red=>{
                // console.log(red.data);
                this.foot_list = red.data
              }).catch(error=>{
                console.log(error.response)
              })
            }
          }
    }
</script>

<style scoped>
    .footer {
        width: 100%;
        height: 128px;
        background: #25292e;
        color: #fff;
    }

    .footer ul {
        margin: 0 auto 16px;
        padding-top: 38px;
        width: 810px;
    }

    .footer ul li {
        float: left;
        width: 112px;
        margin: 0 10px;
        text-align: center;
        font-size: 14px;
    }

    .footer ul::after {
        content: "";
        display: block;
        clear: both;
    }

    .footer p {
        text-align: center;
        font-size: 12px;
    }
</style>
