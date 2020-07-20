<template>
    <div class="cart_item">
        <div class="cart_column column_1">
            <el-checkbox class="my_el_checkbox" v-model="course.selected"></el-checkbox>
        </div>
        <div class="cart_column column_2">
            <img src="/static/image/python.jpg" alt="">
            <span><router-link :to="'/course/detail/'+course.id">{{course.name}}</router-link></span>
        </div>
        <div class="cart_column column_3">
            <el-select v-model="course.expire_id" size="mini" placeholder="请选择购买有效期" class="my_el_select">
                <el-option
                    :label="item.expire_text" :value="item.id" :key="item.id" v-for="item in course.expire_list">
                </el-option>
            </el-select>
        </div>
        <div class="cart_column column_4">{{course.price.toFixed(2)}}</div>
        <div class="cart_column column_4">
            <button @click="dele">删除</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CartItem",
        props: ["course"],
        watch: {
            "course.selected": function () {
                this.cange_select()
            },
            "course.expire_id": function () {
                this.change_expire()
            }

        },
        methods: {
            check_token() {
                let token = localStorage.user_token || sessionStorage.user_token;
                if (!token) {
                    let self = this;
                    this.$confirm("请登录后进行操作", {
                        callback() {
                            self.$router.push("/home/login");
                        }
                    });
                    return false
                }
                return token
            },
            cange_select() {
                let token = this.check_token();
                this.$axios.patch(`${this.$settings.HOST}add/add_cart/`,
                    {selected: this.course.selected, course_id: this.course.id},
                    {
                        headers: {"Authorization": "jwt " + token,}
                    }).then(red => {
                    console.log(red.data);
                    this.$emit("select");
                    this.$message({
                        message: red.data.message,
                        type: 'success'
                    });
                }).catch(eroor => {
                    console.log(eroor.response)
                })
            },
            dele() {
                let token = this.check_token();
                this.$axios.put(`${this.$settings.HOST}add/add_cart/`,
                    {course_id: this.course.id},
                    {
                        headers: {"Authorization": "jwt  " + token}
                    }).then(red => {
                    console.log(red.data.message);
                    this.$message({
                        message: red.data.message,
                        type: 'success'
                    });
                    this.$emit("delete");
                    // this.$emit("select");
                }).catch(eroor => {
                    console.log(eroor.response);
                    console.log(this.token)
                })
            },
            // 切换有效期
            change_expire() {
                let token = this.check_token();
                this.$axios.post(`${this.$settings.HOST}add/add_data/`, {
                    expire_id: this.course.expire_id,
                    course_id: this.course.id
                }, {
                    headers: {
                        "Authorization": "jwt " + token,
                    }
                }).then(response => {
                    console.log(response.data);

                    // 更新切换有效期后课程的价格
                    this.course.price = response.data.price;
                    this.$emit("select");

                    this.$message.success("切换有效期成功");
                }).catch(error => {
                    console.log(error);
                })
            },
        },
        data() {
            return {
                expire: "一个月有效",
            }
        }
    }
</script>

<style scoped>
    .cart_item::after {
        content: "";
        display: block;
        clear: both;
    }

    .cart_column {
        float: left;
        height: 250px;
    }

    .cart_item .column_1 {
        width: 88px;
        position: relative;
    }

    .my_el_checkbox {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        top: 0;
        margin: auto;
        width: 16px;
        height: 16px;
    }

    .cart_item .column_2 {
        padding: 67px 10px;
        width: 520px;
        height: 116px;
    }

    .cart_item .column_2 img {
        width: 175px;
        height: 115px;
        margin-right: 35px;
        vertical-align: middle;
    }

    .cart_item .column_3 {
        width: 197px;
        position: relative;
        padding-left: 10px;
    }

    .my_el_select {
        width: 117px;
        height: 28px;
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
    }

    .cart_item .column_4 {
        padding: 67px 10px;
        height: 116px;
        width: 142px;
        line-height: 116px;
    }

</style>

