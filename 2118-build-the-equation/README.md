<h2><a href="https://leetcode.com/problems/build-the-equation/">2118. Build the Equation</a></h2><h3>Hard</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Terms</code></p>

<pre>+-------------+------+
| Column Name | Type |
+-------------+------+
| power       | int  |
| factor      | int  |
+-------------+------+
power is the primary key column for this table.
Each row of this table contains information about one term of the equation.
power is an integer in the range [0, 100].
factor is an integer in the range [-100, 100] and cannot be zero.
</pre>

<p>&nbsp;</p>

<p>You have a very powerful program that can solve any equation of one variable in the world. The equation passed to the program must be formatted as follows:</p>

<ul>
	<li>The left-hand side (LHS) should contain all the terms.</li>
	<li>The right-hand side (RHS) should be zero.</li>
	<li>Each term of the LHS should follow the format <code>"&lt;sign&gt;&lt;fact&gt;X^&lt;pow&gt;"</code>&nbsp;where:
	<ul>
		<li><code>&lt;sign&gt;</code> is either <code>"+"</code> or <code>"-"</code>.</li>
		<li><code>&lt;fact&gt;</code> is the <strong>absolute value</strong> of the <code>factor</code>.</li>
		<li><code>&lt;pow&gt;</code> is the value of the <code>power</code>.</li>
	</ul>
	</li>
	<li>If the power is <code>1</code>, do not add <code>"^&lt;pow&gt;"</code>.
	<ul>
		<li>For example, if <code>power = 1</code> and <code>factor = 3</code>, the term will be <code>"+3X"</code>.</li>
	</ul>
	</li>
	<li>If the power is <code>0</code>, add neither <code>"X"</code> nor <code>"^&lt;pow&gt;"</code>.
	<ul>
		<li>For example, if <code>power = 0</code> and <code>factor = -3</code>, the term will be <code>"-3"</code>.</li>
	</ul>
	</li>
	<li>The powers in the LHS should be sorted in <strong>descending order</strong>.</li>
</ul>

<p>Write an SQL query to build the equation.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Terms table:
+-------+--------+
| power | factor |
+-------+--------+
| 2     | 1      |
| 1     | -4     |
| 0     | 2      |
+-------+--------+
<strong>Output:</strong> 
+--------------+
| equation     |
+--------------+
| +1X^2-4X+2=0 |
+--------------+
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> 
Terms table:
+-------+--------+
| power | factor |
+-------+--------+
| 4     | -4     |
| 2     | 1      |
| 1     | -1     |
+-------+--------+
<strong>Output:</strong> 
+-----------------+
| equation        |
+-----------------+
| -4X^4+1X^2-1X=0 |
+-----------------+
</pre>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What will be changed in your solution if the power is not a primary key but each power should be unique in the answer?</p>
</div>