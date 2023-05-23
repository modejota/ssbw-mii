import TasksTable from './components/TasksTable'
import Dogs from './components/Dogs';

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
  const [textFieldValue, setTextFieldValue] = useState('')

  const addTask = () => {
    setTasks([...tasks, { title: textFieldValue, status: 'Incomplete' }])
    setTextFieldValue('')
  }

  const handleTextFieldChange = (event) => {
    setTextFieldValue(event.target.value)
  }

  const changeTaskStatus = (index) => {
    setTasks(prevTasks => {
      const newTasks = [...prevTasks];
      newTasks[index].status = newTasks[index].status === 'Complete' ? 'Incomplete' : 'Complete';
      return newTasks;
    });
  }

  const deleteTask = (index) => {
    setTasks(tasks.filter((task, i) => i !== index))
  }

  return (
    <Container maxWidth="m">
      <Dogs />
      <TableContainer component={Paper} style={{ marginTop: '3vh' }}>
        <TasksTable tasks={tasks} handleDelete={deleteTask} changeTaskStatus={changeTaskStatus} handleAdd={addTask}
          textFieldValue={textFieldValue} handleTextFieldChange={handleTextFieldChange} />
      </TableContainer>
    </Container>
  )
}

export default App
