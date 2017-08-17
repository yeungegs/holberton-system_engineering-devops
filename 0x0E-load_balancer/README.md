0-custom_http_response-header
1-install_load_balancer
<!-- Task Body -->
  <p>In this first task you need to configure <code>web-02</code> to be identical to <code>web-01</code>. Fortunately, you built a Bash script during your <a href="https://intranet.hbtn.io/projects/266">web server project</a>, and they&#39;ll now come in handy to easily configure <code>web-02</code>. Remember, always try to automate your work!</p>

<p>Since we&#39;re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p>

<p>Requirements:</p>

<ul>
<li>Configure Nginx so that its HTTP response contains a custom header</li>
<li>The name of the custom HTTP header must be <code>X-Served-By</code></li>
<li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
<li><a href="https://github.com/koalaman/shellcheck/wiki/Ignore">Ignore</a> <a href="https://github.com/koalaman/shellcheck/wiki/SC2154">SC2154</a> for <code>shellcheck</code></li>
<li>Using the Bash scripts you built for your <a href="https://intranet.hbtn.io/projects/266">web server</a>, write <code>0-custom_http_response-header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

<p>Example:</p>

<!-- Task Body -->
  <p>Install and configure HAproxy on your <code>lb-01</code> server.</p>

<p>Requirements:</p>

<ul>
<li>Configure HAproxy with version equal or greater than 1.5 so that it send traffic to <code>web-01</code> and <code>web-02</code></li>
<li>Distribute requests using a roundrobin algorithm</li>
<li>Make sure that HAproxy can be managed via an init script</li>
<li>Make sure that your servers are configured with the right hostnames: <code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>. If not, follow this <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html">tutorial</a>.</li>
<li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul>

<p>Example:</p>

