import TasksTable from './components/TasksTable'

import TableContainer from '@mui/material/TableContainer';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';

import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <Container maxWidth="m">
      <TableContainer component={Paper}>
        <TasksTable />
      </TableContainer>
    </Container>
  )
}

export default App
