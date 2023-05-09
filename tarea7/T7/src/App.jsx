import TasksTable from './components/TasksTable'

import TableContainer from '@mui/material/TableContainer';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';

import React, { useState } from 'react'
import './App.css'

const tasks_init = [
  { title: 'Install', status: 'Complete', },
  { title: 'Create', status: 'Complete', },
  { title: 'Code', status: 'Incomplete', },
  { title: 'Deploy', status: 'Incomplete', },
]


function App() {

  const [tasks, setTasks] = useState(tasks_init)

  const deleteTask = (index) => {
    setTasks(tasks.filter((task, i) => i !== index))
  }

  return (
    <Container maxWidth="m">
      <TableContainer component={Paper}>
        <TasksTable tasks={tasks} handleDelete={deleteTask}/>
      </TableContainer>
    </Container>
  )
}

export default App
