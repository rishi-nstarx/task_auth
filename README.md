<h1>Task Auth</h1>

<p>This repository contains the code for the Task Auth application. Follow the instructions below to set up and run the application.</p>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Ensure you have Docker and Docker Compose installed on your machine.</li>
</ul>

<h3>Clone the Repository</h3>
<p>First, clone the repository to your local machine:</p>

<pre><code>git clone https://github.com/rishi-nstarx/task_auth.git
cd task_auth
</code></pre>

<h3>Build and Run the Application</h3>
<p>Use Docker Compose to build and run the application:</p>

<pre><code>docker-compose build
docker-compose up
</code></pre>

<h3>Apply Migrations</h3>
<p>Once the application is running, access the <code>web_app</code> container to apply the migrations:</p>

<ol>
  <li>Open a new terminal window or tab.</li>
  <li>Execute the following command to access the <code>web_app</code> container:</li>
</ol>

<pre><code>docker exec -it web_container_id/name bash
</code></pre>

<ol start="3">
  <li>Inside the container, run the following commands:</li>
</ol>

<pre><code>python manage.py makemigrations auth_app
python manage.py migrate
</code></pre>

<h3>Access the Application</h3>
<p>After completing the above steps, your application should be up and running.</p>

<h3>Run on browser.</h3>
<p>http://localhost:8000</p>

