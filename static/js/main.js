/*define verify rules*/
const isnum = /^[0-9]*$/;
const isphone = /^[1][3,4,5,6,7,8,9][0-9]{9}$/;
const ismail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
const issfz = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;


const myMixin = {
    methods: {
        handleEdit(title, url, width, height) {

            xadmin.open(title, url, width, height)
        },
        handleEditadd(title, url) {

            xadmin.add_tab(title, url)
        },
        handleEditall(url) {

            xadmin.open('编辑', url, '', '', true)
        },
        handleEditdef(title, url) {

            xadmin.open(title, url)
        },
        //delete
        handleDelete(index, id) {
            var that = this


                that.$confirm('Are you sure to delete it?', 'warning', {
                    confirmButtonText: 'sure',
                    cancelButtonText: 'cancel',
                    type: 'warning'
                }).then(() => {


                    let params = {
                        tablename: that.tablename,
                        idname: that.idname,
                        id: id,

                    }

                    axios({
                        url: '/api/del_one',
                        method: 'post',
                        data: params
                    })
                        .then(function (obj) {

                            that.tableData.splice(index, 1);


                        })

                    this.$message({
                        type: 'success',
                        message: 'success!'
                    });

                })


        },
        //add
        add_one() {
            var that = this

            let params = {
                data: that.datas,
                tablename: that.tablename

            }

            axios({
                url: '/api/add_one',
                method: 'post',
                data: params
            })
                .then(function (obj) {

                    if (obj.data.code == 1) {
                        that.$message({
                            type: 'success',
                            message: 'success!'
                        });
                        setTimeout(function () {
                            location.reload()
                        }, 2.5 * 1000);//延迟2500毫秒

                    }
                     if (obj.data.code == 0) {

                        that.$message({
                            type: 'error',
                            message: 'fail!'
                        });


                    }
                })
        },
        //edit
        edit_one() {
            var that = this

            let params = {
               data: that.datas,
                tablename:that.tablename,
                idname:that.idname,
                id:that.datas[that.idname]
            }

            axios({
                url: '/api/edit_one',
                method: 'post',
                data: params
            })
                .then(function (obj) {

                    if (obj.data.code == 1) {

                        that.$message({
                            type: 'success',
                            message: 'success!'
                        });
                       // setTimeout(function () {
                           // location.reload()
                       // }, 2.5 * 1000);//延迟2500毫秒

                    }
                    if (obj.data.code == 0) {

                        that.$message({
                            type: 'error',
                            message: 'fail!'
                        });


                    }
                })
        },
        //search
        serch() {
            this.dataListFn(1)
        },

        //close
        close() {
            //console.log(this.datas)

            xadmin.close();
                                            xadmin.father_reload();
        },

        btnClick(data) {//page click
            if (data != this.cur) {
                this.cur = data
            }

            this.dataListFn(this.cur.toString());
        },
        pageClick() {
            this.dataListFn(this.cur.toString());
        }

    },
    computed: {
        indexs: function () {
            var left = 1;
            var right = this.all;
            var ar = [];
            if (this.all >= 5) {
                if (this.cur > 3 && this.cur < this.all - 2) {
                    left = this.cur - 2
                    right = this.cur + 2
                } else {
                    if (this.cur <= 3) {
                        left = 1
                        right = 5
                    } else {
                        right = this.all
                        left = this.all - 4
                    }
                }
            }
            while (left <= right) {
                ar.push(left)
                left++
            }
            return ar
        }
    }
}


/*define page app*/
const App = {
    delimiters: ["{[", "]}"], 
    data() {
        return {
            message: 'welcome！'

        }
    }
}


//
// myapp.use(ElementPlus);
