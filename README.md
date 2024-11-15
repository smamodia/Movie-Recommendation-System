# Movie-Recommendation-System
<header>
        <h1>Movie Recommendation System</h1>
        <p>This project implements a <strong>movie recommendation system</strong> using the <strong>cosine similarity algorithm</strong>. It employs a content-based filtering approach to recommend movies similar to a user's preferences.</p>
    </header>

    <section>
        <h2>Project Overview</h2>
        <p>
            This system utilizes movie metadata such as genres, keywords, directors, and more to represent each movie as a vector. 
            By calculating <strong>cosine similarity</strong> between these vectors, the system identifies movies that closely match the user's selected movie(s).
        </p>
    </section>

    <section>
        <h2>Features</h2>
        <ul>
            <li><strong>Personalized Recommendations:</strong> Suggests movies based on a user's selection.</li>
            <li><strong>Cosine Similarity Algorithm:</strong> Measures the similarity between movies using vectorized data.</li>
        </ul>
    </section>

    <section>
        <h2>Dependencies</h2>
        <ul>
            <li><strong>Python:</strong> Version 3.x (recommended)</li>
            <li><strong>Libraries:</strong>
                <ul>
                    <li><code>pandas</code>: For data manipulation.</li>
                    <li><code>numpy</code>: For numerical computations.</li>
                    <li><code>scikit-learn</code>: For cosine similarity calculation.</li>
                </ul>
            </li>
        </ul>
    </section>

    <section>
        <h2>Installation</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/smamodia/Movie-Recommendation-System.git</code></pre>
            </li>
            <li>Install the required libraries (replace <code>library_name</code> with the actual library):
                <pre><code>pip install library_name</code></pre>
            </li>
        </ol>
    </section>

    <section>
        <h2>Usage</h2>
        <ol>
            <li>Run the main script (replace <code>script_name.py</code> with the actual script):
                <pre><code>python script_name.py</code></pre>
            </li>
            <li>The script will prompt you for a movie title or ID.</li>
            <li>The script will recommend movies most similar to your selection.</li>
        </ol>
    </section>