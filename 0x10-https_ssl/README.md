0-https_abc
1-world_wide_web
2-haproxy_ssl_termination

<p>As for project <a href="https://intranet.hbtn.io/projects/259">0x07</a>, use numbers in your answer file.</p>

<p>What is HTTPS?</p>

<ol>
<li>A secure version of HTTP</li>
<li>A faster version of HTTP</li>
<li>A superior version of HTTP</li>
</ol>

<p>Why do you need HTTPS?</p>

<ol>
<li>To encrypt credit card and social security number information going between the client and the website servers</li>
<li>To encrypt all communication between the client and the website servers</li>
<li>To accelerate the communication between the client and the website servers</li>
</ol>

<p>You want to setup HTTPS on your website, where shall you place the certificate?</p>

<ol>
<li>In a secure location where nobody can access it</li>
<li>You can host it anywhere but you have to share the link to it on your website</li>
<li>On your website web server(s)</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x10-https_ssl</code></li>
        <li>File: <code>0-https_abc</code></li>
    </ul>



  <div class="student_correction_requests">

    <!-- Button test code -->
      <button class="task_correction_modal btn btn-default " data-task-id="1529" data-toggle="modal" data-target="#task-test-correction-1529-correction-modal">
        Check your code?
      </button>
      <div class="modal fade task_correction_modal" id="task-test-correction-1529-correction-modal">
      <div class="modal-dialog">
          <div class="modal-content">
          <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Correction of "HTTPS ABC"</h4>
          </div>
          <div class="modal-body">
            <div class="actions">
                <center>
                    <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="1529" />
                    <div class="spinner" >
                        <div class="bounce1"></div>
                        <div class="bounce2"></div>
                        <div class="bounce3"></div>
                    </div>
                    <div class="error"></div>
                    <div class="info"></div>
                </center>
            </div>
            <div class="result"></div>
          </div>
          </div><!-- /.modal-content -->
      </div><!-- /.modal-dialog -->
      </div>


    <!-- Button containers -->

  </div>


</div>

          </div>
          <div data-role="task1530" data-position="2">
              <div class=" clearfix gap" id="task-1530">
<span id="user_id" data-id="116"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1530">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1530" data-project-id="276" data-toggle="modal" data-target="#task-1530-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1530-users-done-modal" data-task-id="1530" data-project-id="276">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Students who are done with "World wide web"</h4>
            </div>
            <div class="modal-body">
              <div class="list-group">
              </div>
              <div class="spinner" >
                  <div class="bounce1"></div>
                  <div class="bounce2"></div>
                  <div class="bounce3"></div>
              </div>
              <div class="error"></div>
            </div>
          </div>
        </div>
      </div>

    </div>

  <h4 class="task">
    1. World wide web
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).
Let&#39;s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>

<p>Requirements:</p>

<ul>
<li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li>
<li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li>
<li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li>
<li>Your Bash script must accept 2 arguments:

<ol>
<li><code>domain</code>:

<ul>
<li> type: string</li>
<li> what: domain name to audit</li>
<li>mandatory: yes</li>
</ul></li>
<li><code>subdomain</code>:

<ul>
<li>type: string</li>
<li>what: specific subdomain to audit</li>
<li>mandatory: no</li>
</ul></li>
</ol></li>
<li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
<li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code></li>
<li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li>
<li>Ignore <code>shellcheck</code> case <code>SC2086</code></li>
<li>Must use: 

<ul>
<li><code>awk</code></li>
<li>at least one Bash function</li>
</ul></li>
<li>You do not need to handle edge cases such as:

<ul>
<li>Empty parameters </li>
<li>Nonexistent domain names</li>
<li>Nonexistent subdomains</li>
</ul></li>
</ul>

<p>Example:</p>

<!-- Task Body -->
  <p>&quot;Terminating SSL on HAproxy&quot; means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to the next hope.</p>

<p>Create a certificate using <code>certbot</code> and configure <code>HAproxy</code> to accept encrypted traffic for your subdomain <code>www.</code>.</p>

<p>Requirements:</p>

<ul>
<li>HAproxy must be listening on port TCP 443</li>
<li>HAproxy must be accepting SSL traffic</li>
<li>HAproxy must serve encrypted traffic that will return the <code>/</code> of your web server</li>
<li>When querying the root of your domain name, the page returned must contain <code>Holberton School</code></li>
<li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
</ul>

<p>Make sure to install HAproxy 1.5 or higher, <a href="https://en.wikipedia.org/wiki/TLS_termination_proxy">SSL termination</a> is not available before v1.5.</p>

<p>Example:</p>

