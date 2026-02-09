const API_BASE_URL = 'http://localhost:8000';

        // Load crop types and soil types from API
        async function loadOptions() {
            try {
                const [cropRes, soilRes] = await Promise.all([
                    fetch(`${API_BASE_URL}/api/crop-types`),
                    fetch(`${API_BASE_URL}/api/soil-types`)
                ]);
                
                const cropData = await cropRes.json();
                const soilData = await soilRes.json();
                
                // Populate dropdowns if needed (currently using static options)
                // This can be enhanced to dynamically populate
            } catch (error) {
                console.error('Error loading options:', error);
            }
        }

        document.getElementById('fertilizerForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const formData = {
                n: parseFloat(document.getElementById('n').value),
                p: parseFloat(document.getElementById('p').value),
                k: parseFloat(document.getElementById('k').value),
                temperature: parseFloat(document.getElementById('temperature').value),
                humidity: parseFloat(document.getElementById('humidity').value),
                moisture: parseFloat(document.getElementById('moisture').value),
                soil_type: document.getElementById('soil_type').value,
                crop_type: document.getElementById('crop_type').value
            };

            // Show loading, hide error and result
            document.getElementById('loading').classList.add('show');
            document.getElementById('error').classList.remove('show');
            document.getElementById('result').classList.remove('show');

            try {
                const response = await fetch(`${API_BASE_URL}/api/predict`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();

                if (!response.ok) {
                    throw new Error(data.detail || 'Prediction failed');
                }

                // Display results
                document.getElementById('fertilizerName').textContent = data.predicted_fertilizer;
                document.getElementById('confidence').textContent = `${(data.confidence * 100).toFixed(1)}%`;
                
                // Display probabilities
                const probList = document.getElementById('probabilitiesList');
                probList.innerHTML = '';
                
                // Sort probabilities by value
                const sortedProbs = Object.entries(data.probabilities)
                    .sort((a, b) => b[1] - a[1]);
                
                sortedProbs.forEach(([fertilizer, prob]) => {
                    const probItem = document.createElement('div');
                    probItem.className = 'prob-item';
                    probItem.innerHTML = `
                        <span class="prob-label">${fertilizer}</span>
                        <span class="prob-value">${(prob * 100).toFixed(1)}%</span>
                    `;
                    probList.appendChild(probItem);
                });

                document.getElementById('result').classList.add('show');
                
            } catch (error) {
                document.getElementById('error').textContent = `Error: ${error.message}`;
                document.getElementById('error').classList.add('show');
            } finally {
                document.getElementById('loading').classList.remove('show');
            }
        });

        function resetForm() {
            document.getElementById('fertilizerForm').reset();
            document.getElementById('result').classList.remove('show');
            document.getElementById('error').classList.remove('show');
        }

        // Load options on page load
        loadOptions();