import React, { useState } from 'react';
import { FlatList, StyleSheet, Text, View, TouchableOpacity, Button } from 'react-native';

const ListOfMovies = ({ navigation }) => {

  const startingDataSource = [
    { title: 'Percy Jackson & The Olympians: The Lightning Thief', releaseDate: '2010-02-12' },
    { title: 'Percy Jackson: Sea of Monsters', releaseDate: '2013-08-07' },
    { title: 'The Lion King', releaseDate: '1994-06-24' },
    { title: 'Aladdin', releaseDate: '1992-11-25' },
    { title: 'Frozen', releaseDate: '2013-11-27' },
  ];

  const [movies, setMovies] = useState(startingDataSource);
  const [loading, setLoading] = useState(false); 

  const loadMoreMovies = async () => {
    if (loading) return;

    setLoading(true);
    try {
      
      const response = await fetch('https://reactnative.dev/movies.json');
      const data = await response.json();

      const newMovies = data.movies.map((movie) => ({
        title: movie.title,
        releaseDate: movie.releaseYear, 
      }));

      setMovies((prevMovies) => [...prevMovies, ...newMovies]);
    } catch (error) {
      console.error('Error fetching movies:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={movies}
        keyExtractor={(item, index) => index.toString()} 
        extraData={movies} 
        renderItem={({ item }) => (
          <TouchableOpacity
            style={[styles.item, styles.border]}
            onPress={() => navigation.navigate('MovieDetails', { movie: item })}
          >
            <Text style={styles.title}>{item.title}</Text>
          </TouchableOpacity>
        )}
      />

      <Button
        title={loading ? 'Loading...' : 'Load More'}
        onPress={loadMoreMovies}
        disabled={loading}
      />
    </View>
  );
};

// Styles for the component
const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 50,
  },
  item: {
    padding: 10,
    fontSize: 18,
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  border: {
    borderWidth: 1,
    borderColor: 'gray',
    marginVertical: 5,
    borderRadius: 5,
  },
});

export default ListOfMovies;
