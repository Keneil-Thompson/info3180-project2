/* Add your Application JavaScript */
const app = Vue.createApp({
    data() {
        return {

        }
    }
});

app.component('app-header', {
    name: 'AppHeader',
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Lab 7</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
		  <li class="nav-item active">
            <router-link class="nav-link" to="/register">Register <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
      </div>
    </nav>
    `
});

app.component('app-footer', {
    name: 'AppFooter',
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; {{ year }} Flask Inc.</p>
        </div>
    </footer>
    `,
    data() {
        return {
            year: (new Date).getFullYear()
        }
    }
});

const Home = {
    name: 'Home',
    template: `
    <div class="jumbotron">
        <h1>Lab 7</h1>
        <p class="lead">In this lab we will demonstrate VueJS working with Forms and Form Validation from Flask-WTF.</p>
    </div>
    `,
    data() {
        return {}
    }
};

const register = {
	name: 'register',
	template:`
	<h1>Registration</h1>
	<form id="UserForm" method = "POST" enctype = "multipart/form-data" v-on:submit.prevent="uploadPhoto">
	<label>Username:</label>
	<textarea name="username"></textarea><br>
	<label>Password:</label>
	<textarea name="password"></textarea><br>
	<label>Name:</label>
	<textarea name="name"></textarea><br>
	<label>Email:</label>
	<textarea name="email"></textarea><br>
	<label>Location:</label>
	<textarea name="location"></textarea><br>
	<label>Biography:</label>
	<textarea name="biography"></textarea><br>
	<label>Photo:</label>
	<input type="file" name ="photo">
	<button class="btn btn-primary mb-2" >Register</button>
	</form>
	`,
	methods:{
		uploadPhoto(){
		let userForm = document.getElementById('UserForm');
		let form_data = new FormData(userForm);
		fetch("/api/register", {
			 method: 'POST',
			 body:form_data,
			 headers:{
				 'X-CSRFToken': token
			 },
			 credentials: 'same-origin'
			})
			 .then(function (response) {
			 return response.json();
			 })
			 .then(function (jsonResponse) {
			 // display a success message
			 console.log(jsonResponse);
			 })
			 .catch(function (error) {
			 console.log(error);
			 });
		}
	},
};

const NotFound = app.component('not-found', {
    template: `
    <div>
        <h1>404 - Not Found</h1>
    </div>
    `,
    data: function () {
        return {}
    }
})

const routes = [
   {path: "/", component: Home},
        // Put other routes here
        {path: "/register", component: register}

        /*{path: "/login", component: Login},

        {path: "/logout", component: Logout},

        {path: "/explore", component: Explore},

        {path: "/users/:user_id", component: MyProfile, props: true},

        {path: "/posts/new", component: NewPosts},*/

        // This is a catch all route in case none of the above matches
];


const router = VueRouter.createRouter({
    history: VueRouter.createWebHistory(),
    routes, // short for `routes: routes`
});

app.use(router);

app.mount('#app');