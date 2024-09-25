<template>
    <div class="container">
        <div class="box">
            <div role="dialog">

                <head>
                    <h5> Personal Information</h5>
                </head>

                <body>
                    <dl>
                        <dd> First Name: </dd>
                        <dd> Last Name: </dd>
                        <dd> Email: </dd>
                        <dd> Phone Number: <span> Gender: </span> </dd>
                    </dl>
                    <hr>
                    <h6> Address</h6>

                    <dl>
                        <dd>
                            <span> City:</span>
                            <span> Country:</span>
                        </dd>
                        <dd>
                            <span> State:</span>
                            <span> Zipcode:</span>
                        </dd>
                    </dl>
                    <hr>
                    <h6> Work Experience: </h6>
                    <dl>
                        <dd>
                            Education Level
                        </dd>
                        <dd>
                            <span> Years of Experience:</span>
                            <span> Job Title:</span>
                        </dd>
                    </dl>
                    <hr>
                    <h6> Application Details</h6>
                    <dl>
                        <dd> Supplier Name: </dd>
                        <dd> Customer Name: </dd>
                        <dd> Applicant ID: </dd>
                        <dd> Appplication Date: </dd>
                        <dd> Application: </dd>
                    </dl>

                </body>
                <footer>
                    <button class = "btn btn-secondary btn-sm btn-block" @click="$event => $emit('close')">
                        Close
                    </button>
                </footer>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    
}
</script>
<style>
.container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #000;
}

.container>div {
    padding: 50px;
    border-radius: 10px;
    border: black;
    background: whitesmoke;
    z-index: 10;
    width: 500px;
    border: 5px black;
}

.btn{   
    position: absolute;
}
    
</style>