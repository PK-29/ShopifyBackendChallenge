
  <!DOCTYPE html>
  <html>

<h1>Backend Intern Challenge - Summer 2018</h1>
<h2>Problem</h2>
<p>Different merchants have different products. Menus are a great way to present
these products in an intuitive way to customers.</p>
<p>To address this we decided to build a system that allows Menus
validation. Our system should be able to aggregate the provided Menus
and identify if any of them contain cyclical references.</p>
<p>Nodes are expressed as objects in a JSON array with the following fields:</p>
<table>
  <thead>
    <th>Fields</th>
    <th>Possible Values</th>
    <th>Optional Values</th>
    <th>Description</th>
  </thead>
  <tbody>
    <tr>
      <td><code>id</code></td>
      <td><code>"number"</code>
      <td></td>
      <td>
        Uniquely identifies each node of the Menu.
      </td>
    </tr>
    <tr>
      <td><code>data</code></td>
      <td><code>"string"</code></td>
      <td></td>
      <td>
        Specifies the data that the node holds.
      </td>
    </tr>
    <tr>
      <td><code>parent_id</code></td>
      <td><code>"number"</code></td>
      <td>&check;</td>
      <td>
        Specifies the parent of the node.
      </td>
    </tr>
    <tr>
      <td><code>child_ids</code></td>
      <td>Array of <code>"number"</code></td>
      <td></td>
      <td>
        Specifies the children of the node.
      </td>
    </tr>
  </tbody>
</table>
<p><strong>API Example Response:</strong></p>
<pre lang="json"><code>{
  &quot;menus&quot;:[
    {
      &quot;id&quot;:1,
      &quot;data&quot;:&quot;House&quot;,
      &quot;child_ids&quot;:[3]
    },
    {
      &quot;id&quot;:2,
      &quot;data&quot;:&quot;Company&quot;,
      &quot;child_ids&quot;:[4]
    },
    {
      &quot;id&quot;:3,
      &quot;data&quot;:&quot;Kitchen&quot;,
      &quot;parent_id&quot;:1,
      &quot;child_ids&quot;:[5]
    },
    {
      &quot;id&quot;:4,
      &quot;data&quot;:&quot;Meeting Room&quot;,
      &quot;parent_id&quot;:2,
      &quot;child_ids&quot;:[6]
    },
    {
      &quot;id&quot;:5,
      &quot;data&quot;:&quot;Sink&quot;,
      &quot;parent_id&quot;:3,
      &quot;child_ids&quot;:[1]
    },
    {
      &quot;id&quot;:6,
      &quot;data&quot;:&quot;Chair&quot;,
      &quot;parent_id&quot;:4,
      &quot;child_ids&quot;:[]
    }
  ],
  &quot;pagination&quot;:{
    &quot;current_page&quot;:1,
    &quot;per_page&quot;:5,
    &quot;total&quot;:19
  }
}
</code></pre>
<h2>API response</h2>
<p>The response will contain the followings keys:</p>
<ul>
<li><code>menus</code> - Array containing nodes that together become Menus.</li>
<li><code>pagination</code> - An object containing the <code>current_page</code>, <code>per_page</code> and <code>total</code> keys</li>
</ul>
<h2>Instructions</h2>
<p><strong>Candidates can use any programming language of their choice.</strong></p>
<p>Obtain a list of Nodes from the API and build the appropriate Menus.
Cycles should be identified and the offending Menus should be marked as invalid.
The max depth of a Menu is <strong>4</strong>.</p>
<p>The output for the given example should be as follows:</p>
<pre lang="json"><code>{
  &quot;valid_menus&quot;: [
    { &quot;root_id&quot;: 2, &quot;children&quot;: [4, 6] },
  ],
  &quot;invalid_menus&quot;: [
    { &quot;root_id&quot;: 1, &quot;children&quot;: [1, 3, 5] }
  ]
}
</code></pre>
<p>The output is expected to be in JSON and to contain the following keys:</p>
<ul>
<li><code>valid_menus</code> - Array containing information about each valid menu:
<ol>
<li><code>root_id</code> - The id of the menu root</li>
<li><code>children</code> - An Array containing all the children belonging to the menu</li>
</ol>
</li>
<li><code>invalid_menus</code> - Array containing information about each invalid menu:
<ol>
<li><code>root_id</code> - The id of the menu root</li>
<li><code>children</code> - An Array containing all the children belonging to the menu</li>
</ol>
</li>
</ul>
<p>The API endpoint can be found at:</p>
<p><a href="https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&amp;page=1">https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&amp;page=1</a></p>
<p>This will return the first page of nodes. You can obtain subsequent pages by incrementing the <code>page</code> query parameter.</p>
<h2>Extra challenge</h2>
<p>The same rules of the original challenge applies.</p>
<p>The API endpoint can be found at:</p>
<p><a href="https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&amp;page=1">https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=2&amp;page=1</a></p>
<p>This will return the first page of nodes. You can obtain subsequent pages by incrementing the <code>page</code> query parameter.</p>


