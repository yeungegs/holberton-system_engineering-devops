irewall_ABC
lock_all_incoming_traffic_but
ort_forwarding
<!-- Task Body -->
  <p>Pick one answer for every question.</p>

<p>What is a firewall?</p>

<ol>
<li>A hardware security system</li>
<li>A hardware or software security system</li>
<li>A software security system</li>
</ol>

<p>What are the 2 types of firewall:</p>

<ol>
<li>Soft and hard firewall</li>
<li>Incoming and outgoing firewall</li>
<li>Network and host-based firewall</li>
</ol>

<p>What is the main function of a firewall?</p>

<ol>
<li>To filter incoming and outgoing network traffic</li>
<li>To filter  incoming and outgoing TCP traffic</li>
<li>To  filter outgoing traffic</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x12-firewall</code></li>
        <li>File: <code>0-firewall_ABC</code></li>
    </ul>



  <div class="student_correction_requests">

    <!-- Button test code -->
      <button class="task_correction_modal btn btn-default " data-task-id="1566" data-toggle="modal" data-target="#task-test-correction-1566-correction-modal">
        Check your code?
      </button>
      <div class="modal fade task_correction_modal" id="task-test-correction-1566-correction-modal">
      <div class="modal-dialog">
          <div class="modal-content">
          <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Correction of "Firewall ABC"</h4>
          </div>
          <div class="modal-body">
            <div class="actions">
                <center>
                    <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="1566" />
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
          <div data-role="task1567" data-position="2">
              <div class=" clearfix gap" id="task-1567">
<span id="user_id" data-id="116"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1567">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1567" data-project-id="284" data-toggle="modal" data-target="#task-1567-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1567-users-done-modal" data-task-id="1567" data-project-id="284">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Students who are done with "Block all incoming traffic but"</h4>
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
    1. Block all incoming traffic but
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Let&#39;s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p>

<p>Requirements:</p>

<ul>
<li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won&#39;t be checked)</li>
<li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:

<ul>
<li><code>22</code> (SSH)</li>
<li><code>443</code> (HTTPS SSL)</li>
<li><code>80</code> (HTTP)</li>
</ul></li>
<li>Share the <code>ufw</code> commands that you used in your answer file</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
    <p class="sm-gap"><strong>Repo:</strong></p>
    <ul>
      <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
        <li>Directory: <code>0x12-firewall</code></li>
        <li>File: <code>1-block_all_incoming_traffic_but</code></li>
    </ul>



  <div class="student_correction_requests">

    <!-- Button test code -->
      <button class="task_correction_modal btn btn-default " data-task-id="1567" data-toggle="modal" data-target="#task-test-correction-1567-correction-modal">
        Check your code?
      </button>
      <div class="modal fade task_correction_modal" id="task-test-correction-1567-correction-modal">
      <div class="modal-dialog">
          <div class="modal-content">
          <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Correction of "Block all incoming traffic but"</h4>
          </div>
          <div class="modal-body">
            <div class="actions">
                <center>
                    <input type="submit" name="commit" value="Start a new test" class="btn btn-primary correction_request_test_admin" data-task-id="1567" />
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
          <div data-role="task1568" data-position="3">
              <div class=" clearfix gap" id="task-1568">
<span id="user_id" data-id="116"></span>

    <div class="student_task_controls">

      <!-- button Done -->
        <button class="student_task_done btn btn-default no" data-task-id="1568">
          <span class="no"><i class="fa fa-square-o"></i></span>
          <span class="yes"><i class="fa fa-check-square-o"></i></span>
          <span class="pending"><i class="fa fa-spinner fa-pulse"></i></span>
          Done<span class="no pending">?</span><span class="yes">!</span>
        </button>
        <br>

      <!-- button Help! -->
      <button class="users_done_for_task btn btn-default btn-default" data-task-id="1568" data-project-id="284" data-toggle="modal" data-target="#task-1568-users-done-modal">
        Help
      </button>
      <div class="modal fade users-done-modal" id="task-1568-users-done-modal" data-task-id="1568" data-project-id="284">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title">Students who are done with "Port forwarding"</h4>
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
    2. Port forwarding
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
  </h4>


  <!-- Progress vs Score -->

<!-- Task Body -->
  <p>Firewalls can not only filter requests, they can also forward them.</p>

<p>Requirements:</p>

<ul>
<li>Configure <code>web-01</code> so that its firewall redirects port <code>8080/TCP</code> to port <code>80/TCP</code>.</li>
<li>Your answer file should be a copy of the <code>ufw</code> configuration file that you modified to make this happen</li>
</ul>

<p>Terminal in <code>web-01</code>:</p>

0-firewall_ABC
1-block_all_incoming_traffic_but
2-port_forwarding
