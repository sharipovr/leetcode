use std::collections::HashMap;
impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        // Create a hash map to group anagrams
        let mut map: HashMap<String, Vec<String>> = HashMap::new();
        // Iterate over each string in the input
        for s in strs {
            // Convert the string to a vector of chars for sroting
            let mut chars: Vec<char> = s.chars().collect();
            // Sort the characters to get the anagram key
            chars.sort_unstable();
            // Convert the sorted chars back to a string
            let key: String = chars.into_iter().collect();
            // Insert the originam string into the correct group in the map
            map.entry(key).or_insert(Vec::new()).push(s);
        }
        // Collect all the grouped anagrams into a vector and return
        map.into_values().collect()
    }
}