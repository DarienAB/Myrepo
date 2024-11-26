import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const MovieDetails = ({ route }) => {
  const { movie } = route.params;

  // Check if movie is passed correctly
  if (!movie) {
    return <Text>Movie details not available</Text>;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{movie.title || 'No title available'}</Text>
      <Text style={styles.releaseDate}>{movie.releaseDate ? `Release Date: ${movie.releaseDate}` : 'Release Date: Not available'}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  },
  releaseDate: {
    fontSize: 18,
    color: 'gray',
  },
});

export default MovieDetails;
