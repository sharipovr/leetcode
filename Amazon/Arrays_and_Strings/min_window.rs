impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        // Convert s and t to byte arrays for easy indexing
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();

        // Frequency table for t
        let mut t_count = [0; 128];     // ASCII
        for &b in t_bytes {
            t_count[b as usize] += 1;   // count each char in t
        } 

        // Number of unique characters in t that must be present in window
        let required = t_count.iter().filter(|&&x| x > 0).count();

        // Window counts and how many chars are satisfied
        let mut window_count = [0; 128];
        let mut formed = 0;     // how manu unique chars in windows match t's requirement

        let mut left = 0;       // Left pointer of window
        let mut right = 0;      // Right pointer of window
        
        let mut min_len = usize::MAX;   // Track min window length
        let mut min_left = 0;           // Track min window star

        while right < s_bytes.len() {
            let b = s_bytes[right];
            window_count[b as usize] += 1;  // Add char to window

            // If this char's count matches t's requirement, increment formed
            if t_count[b as usize] > 0 && window_count[b as usize] == t_count[b as usize] {
                formed += 1;
            }

            // Try to shrink window from the left
            while formed == required {
                // Update min window if smaller
                if right - left + 1 < min_len {
                    min_len = right - left + 1;
                    min_left = left;
                }
                let lb = s_bytes[left];
                window_count[lb as usize] -= 1; // Remove char from window

                // if this char is now less than required, decrement formed
                if t_count[lb as usize] > 0 && window_count[lb as usize] < t_count[lb as usize] {
                    formed -= 1;
                }
                left += 1;  // Move left pointer
            }
            right += 1;     // Move right pointer
        }

        if min_len == usize::MAX {
            "".to_string()  // No window found
        } else {
            s[min_left..min_left+min_len].to_string()   // Return min window substring
        }
    }
}