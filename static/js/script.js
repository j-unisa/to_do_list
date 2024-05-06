function delete_task(task_id)
{
fetch(`/delete_task/${task_id}`,
    {
    method: 'DELETE',
    })
    .then(response => response.json())
    .then(data =>
        {
        console.log(data.message);
        })
    .catch(error =>
        {
        console.error('Error:', error);
        });

        // Remove task from UI
        const list_item = event.target.closest('li');
        list_item.remove();
}